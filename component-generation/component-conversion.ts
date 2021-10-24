import {TypeReference} from '@ts-morph/common/lib/typescript';
import * as ts from 'typescript';
import {customizeComponent, SkippedProperty} from './component-customization';
import {ComponentView, ComponentViewProperty} from './templating';
import {ComponentDefinition, ComponentProperty} from './type-checking';

/**
 * Error thrown when the type for which the `PropType` should be created is a function. Function are not handled and
 * this is what this error is for.
 */
class FunctionTypeError extends Error {}

/**
 * Creates a string representing the `PropType` from the given TypeScript type.
 *
 * @param sourceType The type of the property for which the `PropType` must be created.
 * @param checker The type checker to use.
 * @param propertyName The name of the property for which the type should be created.
 * @returns The `PropType` for this property.
 */
function createPropType(
    sourceType: ts.Type,
    checker: ts.TypeChecker,
    propertyName?: string
): string {
    const typeAsString = checker.typeToString(sourceType);

    if (
        (ts.TypeFlags.Boolean & sourceType.flags) === ts.TypeFlags.Boolean ||
        // It might happen that a boolean property might be declared as only a 'false' or 'true' literal.
        typeAsString === 'false' ||
        typeAsString === 'true'
    ) {
        return 'PropTypes.bool';
    }

    if (ts.TypeFlags.NumberLike & sourceType.flags) {
        return 'PropTypes.number';
    }

    if (ts.TypeFlags.StringLike & sourceType.flags) {
        return 'PropTypes.string';
    }

    if ((ts.TypeFlags.Unknown | ts.TypeFlags.Any) & sourceType.flags) {
        return 'PropTypes.any';
    }

    if (sourceType.getSymbol()?.name === 'Array') {
        const elementType = checker.getTypeArguments(
            sourceType as TypeReference
        )[0];
        const elementPropType = createPropType(elementType, checker);
        return `PropTypes.arrayOf(${elementPropType})`;
    }

    if (typeAsString === 'ReactNode') {
        return propertyName === 'children' ? 'PropTypes.node' : 'PropTypes.any';
    }

    if (typeAsString === 'Element' || typeAsString === 'VirtualElement') {
        return 'PropTypes.element';
    }

    // The `sx` property is always typed as a generic `SxProps<T>`, and Python can't do better than converting those to
    // objects.
    if (/SxProps<.*>/.test(typeAsString)) {
        return 'PropTypes.object';
    }

    if (sourceType.isIntersection()) {
        const intersectionType = sourceType as ts.IntersectionType;

        let intersectsWithFunctionType = false;

        const resolvedTypes = intersectionType.types.flatMap((type) => {
            if (ts.TypeFlags.Literal & type.flags) {
                const value = checker.typeToString(type);
                return [`PropTypes.oneOf([${value}])`];
            }

            try {
                return [createPropType(type, checker)];
            } catch (e) {
                intersectsWithFunctionType =
                    intersectsWithFunctionType ||
                    e instanceof FunctionTypeError;
                return [];
            }
        });

        if (resolvedTypes.length === 0) {
            if (intersectsWithFunctionType) {
                throw new FunctionTypeError(
                    `Failed to find propType for intersection including a function type ${typeAsString}.`
                );
            } else {
                throw new Error(
                    `Failed to find propType for intersection ${typeAsString}.`
                );
            }
        } else {
            let resolvedType = resolvedTypes[0];

            if (resolvedTypes.length > 1) {
                // If there is better than just setting `any`, going for it.
                const nonAnyType = resolvedTypes.find(
                    (type) => type !== 'PropTypes.any'
                );
                resolvedType = nonAnyType ?? resolvedType;
            }

            return resolvedType;
        }
    }

    if (sourceType.isUnion()) {
        const unionType = sourceType as ts.UnionType;

        const typesSet = new Set<string>();
        const valuesSet = new Set<string>();

        unionType.types.forEach((type) => {
            if (ts.TypeFlags.Literal & type.flags) {
                valuesSet.add(checker.typeToString(type));
            } else {
                try {
                    typesSet.add(createPropType(type, checker));
                } catch (e) {
                    return;
                }
            }
        });

        if (valuesSet.size > 0) {
            const valuesType = `PropTypes.oneOf([${[...valuesSet].join(
                ', '
            )}])`;

            if (typesSet.size > 0) {
                typesSet.add(valuesType);
            } else {
                return valuesType;
            }
        }

        if (typesSet.size === 0) {
            console.warn(
                `Could not resolve any types in union ${typeAsString}. Setting as any.`
            );
            return 'PropTypes.any';
        }
        if (typesSet.size === 1) {
            return typesSet.keys().next().value;
        }
        return `PropTypes.oneOfType([${[...typesSet].join(', ')}])`;
    }

    if (ts.TypeFlags.Object & sourceType.flags || typeAsString === 'object') {
        if (sourceType.getCallSignatures().length > 0) {
            throw new FunctionTypeError(
                `${typeAsString} is a function type and should not be exposed.`
            );
        }

        // Trying to define more precisely the object's properties can get messy when there's a lot of them.
        // Simply returning `any` for now.
        return 'PropTypes.any';
    }

    if (
        ts.TypeFlags.TypeParameter & sourceType.flags &&
        propertyName === 'component'
    ) {
        // Classes cannot be passed from Python, but strings can represent base HTML component types.
        return 'PropTypes.string';
    }

    throw new Error(`Failed to find propType for ${typeAsString}.`);
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
                if (property.name.startsWith('aria-')) {
                    throw new Error(`Skipping property ${property.name}.`);
                }

                const propType = createPropType(
                    property.type,
                    checker,
                    property.name
                );

                return {...property, propType, forwardProperty: true};
            } catch (e) {
                skippedProperties.push({
                    ...property,
                    typeAsString,
                    isFunctionType: e instanceof FunctionTypeError,
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
        const skippedPropertiesString = skippedProperties
            .filter((p) => !p.isFunctionType && !p.name.startsWith('aria-'))
            .map((p) => `  - ${p.name}: ${p.typeAsString}`)
            .join('\n');

        if (skippedPropertiesString.length > 0) {
            console.warn(
                `Skipped properties for component ${componentView.name}:\n${skippedPropertiesString}`
            );
        }
    }
    return componentView;
}
