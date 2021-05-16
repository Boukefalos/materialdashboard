import * as Mustache from 'mustache';
import * as fs from 'fs';
import * as path from 'path';

const TEMPLATES_DIR = path.join(__dirname, 'templates');
const COMPONENT_TEMPLATE_FILE = path.join(TEMPLATES_DIR, 'template-component.js');
const INDEX_TEMPLATE_FILE = path.join(TEMPLATES_DIR, 'template-index.js');
const COMPONENT_TEMPLATE = fs.readFileSync(COMPONENT_TEMPLATE_FILE).toString();
const INDEX_TEMPLATE = fs.readFileSync(INDEX_TEMPLATE_FILE).toString();
const MUSTACHE_OPTIONS = { escape: t => t, tags: ['{{', '}}'] as [string, string] };

/**
 * A component property that can be used by the template system.
 */
export interface ComponentViewProperty {
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
     * The `PropType` that will be used in the component property types.
     */
    propType: string;
    /**
     * Whether the property should be forwarded to the underlying material component.
     */
    forwardProperty: boolean;
}

/**
 * A component event that can be used by the template system.
 */
export interface ComponentViewEvent {
    /**
     * The name of the Material-UI component event.
     */
    name: string;
    /**
     * The code / function for this event.
     */
    code: string;
}

/**
 * A component definition that can be used by the template system.
 */
export interface ComponentView {
    /**
     * The name of the component.
     */
    name: string;
    /**
     * Properties for this component.
     */
    properties: ComponentViewProperty[];
    /**
     * Events of the underlying Material-UI component that should be implemented.
     */
    events: ComponentViewEvent[];
    /**
     * Extra imports that should be added at the top of the source file.
     */
    imports: string[];
    /**
     * Additional code that should be added to the component function, before it returns the Material-UI component.
     */
    extraCode: string[];
    /**
     * The code to insert to include children nodes in the component. `{children}` in most cases.
     */
    childrenCode: string;
}

/**
 * Generates the given components and writes them to the disk.
 *
 * @param componentViews The components to generate.
 * @param destinationPath The path where the index file will be created.
 * @param componentDirectory The name of the sub directory in which components will be placed.
 */
export function writeComponents(componentViews: ComponentView[], destinationPath: string,
                                componentDirectory: string): void {
    const componentDirectoryPath = path.join(destinationPath, componentDirectory);

    if (!fs.existsSync(componentDirectoryPath)) {
        fs.mkdirSync(componentDirectoryPath, { recursive: true });
    }

    componentViews.forEach(component => {
        // Mustache is a simple template system, and any "advanced" filtering needs to happen outside of the template.
        const renderedComponent = Mustache.render(COMPONENT_TEMPLATE, {
            ...component,
            propertiesWithDefault: component.properties.filter(p => p.stringDefault),
            privateProperties: component.properties.filter(p => !p.forwardProperty),
            hasChildren: component.properties.findIndex(p => p.name === 'children') >= 0,
        }, undefined, MUSTACHE_OPTIONS);
        const destinationPath = path.join(componentDirectoryPath, `${component.name}.react.js`);
        fs.writeFileSync(destinationPath, renderedComponent);
    });

    const indexView = {
        components: componentViews.map(component => ({
            name: component.name,
            path: `./${componentDirectory}/${component.name}.react`
        }))
    };
    const renderedIndex = Mustache.render(INDEX_TEMPLATE, indexView, undefined, MUSTACHE_OPTIONS);

    const indexPath = path.join(destinationPath, 'index.js');
    fs.writeFileSync(indexPath, renderedIndex);
}
