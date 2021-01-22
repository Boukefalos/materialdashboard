import * as ts from 'typescript';

/**
 * A component property, extracted from its TypeScript definition.
 */
export interface ComponentProperty {
    /**
     * The name of the property.
     */
    name: string;
    /**
     * The documentation for this property.
     */
    documentation: string[];
    /**
     * The default value for this property, as a string that can be inserted into the source code for the component.
     */
    stringDefault: string;
    /**
     * The TypeScript Type for this property.
     */
    type: ts.Type;
}

/**
 * A component definition extracted from its TypeScript definition.
 */
export interface ComponentDefinition {
    /**
     * The name of the component.
     */
    name: string;
    /**
     * The properties of the component.
     */
    properties: ComponentProperty[];
}

/**
 * Extracts the properties from a component TypeScript type.
 *
 * @param componentType The TypeScript Type for the component.
 * @param checker The type checker to use.
 * @returns The list of properties for the component.
 */
function getPropertiesFromComponentType(componentType: ts.Type, checker: ts.TypeChecker): ComponentProperty[] {
    // The component is a callable...
    const callSignatures = componentType.getCallSignatures()
    if (callSignatures.length === 0) {
        throw new Error('Expected to find a call signature for component.');
    }

    // ...its first (and single) argument should be the component properties...
    const componentFuncSignature = callSignatures[0];
    const callParameters = componentFuncSignature.getParameters();
    if (callParameters.length !== 1) {
        throw new Error('Expected to find a call signature with a single props parameter for component.');
    }
    const propsParameter = callParameters[0];

    // ...and it should return an element.
    const returnType = componentFuncSignature.getReturnType();
    if (checker.typeToString(returnType) !== 'Element') {
        // TODO(flo): Make this check more robust.
        throw new Error('Component function should return a JSX.Element.')
    }

    // Getting the fully resolved type of the `props` parameter.
    const propsType = checker.getTypeOfSymbolAtLocation(propsParameter, propsParameter.valueDeclaration);

    // Listing available properties for the component.
    const props = propsType.getProperties();

    return props.map(p => {
        return {
            name: p.name,
            documentation: p.getDocumentationComment(checker).flatMap(c => c.text.split('\n')),
            // TODO(flo): This needs more work as the defaults might be values other than literals, which will fail to
            // resolve once inserted in the generated component.
            // stringDefault: p.getJsDocTags().find(t => t.name === 'default')?.text,
            stringDefault: '',
            type: checker.getTypeOfSymbolAtLocation(p, propsParameter.valueDeclaration)
        }
    });
}

/**
 * Creates a component definition from a TypeScript node by extracting the defined properties for this component.
 *
 * @param name The name of the component to create.
 * @param node The TypeScript node containing the component declaration.
 * @param checker The type checker to use.
 * @returns The component definition.
 */
export function createComponentFromNode(name: string, node: ts.Node, checker: ts.TypeChecker): ComponentDefinition {
    const declarationType = checker.getTypeAtLocation(node);
    const properties = getPropertiesFromComponentType(declarationType, checker);
    return { name, properties };
}
