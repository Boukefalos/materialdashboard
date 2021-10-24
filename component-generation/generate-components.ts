import * as path from 'path';
import {Project, SourceFile} from 'ts-morph';
import * as ts from 'typescript';
import {createView} from './component-conversion';
import {ComponentView, writeComponents} from './templating';
import {ComponentNotFound, createComponentFromNode} from './type-checking';

// TypeScript definitions for Material-UI, including all available components.
const INDEX_FILE = require.resolve('@mui/material/index.d.ts');
const DESTINATION_PATH = path.join(__dirname, '..', 'src', 'lib');
const COMPONENTS_DIRECTORY = 'components';

/**
 * Analyzes the given source file and returns a list of component views, that can be used to generate Dash components.
 *
 * @param sourceFile The ts-morph source file containing the component definitions.
 * @param checker The TypeScript type checker to use to analyse the source file.
 * @returns A list of component views.
 */
function getViewsForExportedComponentsInSourceFile(
    sourceFile: SourceFile,
    checker: ts.TypeChecker
): ComponentView[] {
    const declarations = sourceFile.getExportedDeclarations();

    const componentViews: ComponentView[] = [];
    declarations.forEach((keyDeclarations, key) => {
        const declaration = keyDeclarations[0];

        try {
            const component = createComponentFromNode(
                key,
                declaration.compilerNode,
                checker
            );

            console.log(`Creating view for component ${key}...`);

            const componentView = createView(component, checker);
            componentViews.push(componentView);
        } catch (e) {
            if (e instanceof ComponentNotFound) {
                // Some of the declarations not being components is expected. They should simply be ignored.
                return;
            }

            console.error(
                `Error while extracting component from declaration ${key}: ${e}`
            );
        }
    });

    return componentViews;
}

function main() {
    const project = new Project();
    const sourceFile = project.addSourceFileAtPath(INDEX_FILE);
    const checker = project.getTypeChecker().compilerObject;

    const componentViews = getViewsForExportedComponentsInSourceFile(
        sourceFile,
        checker
    );
    writeComponents(componentViews, DESTINATION_PATH, COMPONENTS_DIRECTORY);
}

main();
