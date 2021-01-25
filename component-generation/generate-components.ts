import * as path from 'path';
import * as ts from 'typescript';
import { Project, SourceFile } from 'ts-morph';

import { createView } from './component-conversion';
import { ComponentView, writeComponents } from './templating';
import { createComponentFromNode } from './type-checking';

// TypeScript definitions for Material-UI, including all available components.
const INDEX_FILE = require.resolve('@material-ui/core/index.d.ts');
const DESTINATION_PATH = path.join(__dirname, '..', 'src', 'lib');
const COMPONENTS_DIRECTORY = 'components';

/**
 * Analyzes the given source file and returns a list of component views, that can be used to generate Dash components.
 *
 * @param sourceFile The ts-morph source file containing the component definitions.
 * @param checker The TypeScript type checker to use to analyse the source file.
 * @returns A list of component views.
 */
function getViewsForExportedComponentsInSourceFile(sourceFile: SourceFile, checker: ts.TypeChecker): ComponentView[] {
    const declarations = sourceFile.getExportedDeclarations();

    const componentViews: ComponentView[] = [];
    declarations.forEach((keyDeclarations, key) => {
        const declaration = keyDeclarations[0];

        try {
            console.log(`Trying to extract component from declaration ${key}...`);

            const component = createComponentFromNode(key, declaration.compilerNode, checker);
            const componentView = createView(component, checker);
            componentViews.push(componentView);
        } catch (e) {
            console.warn(`Error while extracting component from declaration ${key}: ${e}`);
        }
    });

    return componentViews;
}

function main() {
    const project = new Project();
    const sourceFile = project.addSourceFileAtPath(INDEX_FILE);
    const checker = project.getTypeChecker().compilerObject;

    const componentViews = getViewsForExportedComponentsInSourceFile(sourceFile, checker);
    writeComponents(componentViews, DESTINATION_PATH, COMPONENTS_DIRECTORY);
}

main();
