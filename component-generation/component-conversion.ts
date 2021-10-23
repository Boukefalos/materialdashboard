import {TypeReference} from '@ts-morph/common/lib/typescript';
import * as ts from 'typescript';
import {customizeComponent, SkippedProperty} from './component-customization';
import {ComponentView, ComponentViewProperty} from './templating';
import {ComponentDefinition, ComponentProperty} from './type-checking';

/**
 * Creates a string representing the `PropType` from the given TypeScript type.
 *
 * @param sourceType The type of the property for which the `PropType` must be created.
 * @param checker The type checker to use.
 * @param allowComplexTypes Whether complex types, like React nodes or union are allowed (useful when this is called
 *     recursively, but we don't want to allow more than one recursion).
 * @returns The `PropType` for this property.
 */
function createPropType(
    sourceType: ts.Type,
    checker: ts.TypeChecker,
    allowComplexTypes = true
): string {
    const typeAsString = checker.typeToString(sourceType);

    function fail() {
        throw new Error(`Failed to find propType for ${typeAsString}.`);
    }

    if (
        (ts.TypeFlags.Boolean & sourceType.flags) === ts.TypeFlags.Boolean ||
        // It might happen that a boolean property might be declared as only a 'false' or 'true' literal.
        typeAsString === 'false'
    ) {
        return 'PropTypes.bool';
    }

    if (
        ts.TypeFlags.NumberLike & sourceType.flags ||
        typeAsString === 'number & {}'
    ) {
        return 'PropTypes.number';
    }

    if (
        ts.TypeFlags.StringLike & sourceType.flags ||
        typeAsString === 'string & {}'
    ) {
        return 'PropTypes.string';
    }

    if ((ts.TypeFlags.Unknown | ts.TypeFlags.Any) & sourceType.flags) {
        return 'PropTypes.any';
    }

    if (sourceType.getSymbol()?.name === 'Array') {
        const elementType = checker.getTypeArguments(
            sourceType as TypeReference
        )[0];
        const elementPropType = createPropType(elementType, checker, true);
        return `PropTypes.arrayOf(${elementPropType})`;
    }

    if (!allowComplexTypes) {
        fail();
    }

    if (typeAsString === 'ReactNode') {
        return 'PropTypes.node';
    }

    // The `sx` property is always typed as a generic `SxProps<T>`, and in Python can't do better than converting those
    // to objects.
    if (/SxProps<.*>/.test(typeAsString)) {
        return 'PropTypes.object';
    }

    if (sourceType.isUnion()) {
        const unionType = sourceType as ts.UnionType;

        // If at least one of the types is not a literal, we'll need to recursively determine the types that are
        // allowed. If all types are literal, we can simply list the values and be done with it.
        if (
            unionType.types.findIndex(
                (t) => (ts.TypeFlags.Literal & t.flags) === 0
            ) >= 0
        ) {
            const types = unionType.types.map((t) =>
                createPropType(t, checker, false)
            );
            return `PropTypes.oneOfType([${types.join(', ')}])`;
        } else {
            const values = unionType.types.map((t) => checker.typeToString(t));
            return `PropTypes.oneOf([${values.join(', ')}])`;
        }
    }

    fail();
}

/**
 * Converts a list of properties extracted from TypeScript definitions to property "views" that can be used for Dash
 * component generation.
 *
 * @param properties The properties to convert.
 * @param checker The type checker to use.
 * @returns The property "views".
 */
function convertComponentPropertiesToView(
    properties: ComponentProperty[],
    checker: ts.TypeChecker
): {
    viewProperties: ComponentViewProperty[];
    skippedProperties: SkippedProperty[];
} {
    const skippedProperties: SkippedProperty[] = [];

    const viewProperties: ComponentViewProperty[] = properties.flatMap(
        (property) => {
            const typeAsString = checker.typeToString(property.type);

            try {
                if (
                    ['component', 'innerRef'].includes(property.name) ||
                    property.name.startsWith('aria-')
                ) {
                    throw new Error(`Skipping property ${property.name}.`);
                }

                let propType: string;
                // TODO(flo): Move inside `createPropType`.
                if (
                    typeAsString === 'ReactNode' &&
                    property.name !== 'children'
                ) {
                    // Dash only supports the `children` property to pass child nodes. However other `ReactNode` properties
                    // might still be worth exposing as `any` such that we can still pass a string to them for example.
                    console.warn(
                        `Defining node property ${property.name} as any instead of ReactNode.`
                    );
                    propType = 'PropTypes.any';
                } else {
                    propType = createPropType(property.type, checker);
                }

                return {...property, propType, forwardProperty: true};
            } catch (e) {
                skippedProperties.push({
                    ...property,
                    typeAsString,
                });
            }

            return [];
        }
    );

    return {viewProperties, skippedProperties};
}

/**
 * Create a component view from a component definition extracted from TypeScript.
 *
 * @param componentDefinition The component extracted from TypeScript definitions.
 * @param checker The type checker to use.
 * @returns The component view.
 */
export function createView(
    componentDefinition: ComponentDefinition,
    checker: ts.TypeChecker
): ComponentView {
    const {viewProperties, skippedProperties} =
        convertComponentPropertiesToView(
            componentDefinition.properties,
            checker
        );

    const componentView: ComponentView = {
        name: componentDefinition.name,
        properties: viewProperties,
        events: [],
        imports: [],
        extraCode: [],
        childrenCode: '{children}',
    };
    customizeComponent(componentView, skippedProperties);

    if (skippedProperties.length > 0) {
        const skippedPropertiesNames = skippedProperties
            .map((p) => p.name)
            .join(', ');
        console.warn(
            `Skipped properties for component ${componentView.name}: ${skippedPropertiesNames}`
        );
    }
    return componentView;
}
