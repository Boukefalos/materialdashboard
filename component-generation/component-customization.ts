import * as fs from 'fs';
import * as path from 'path';

import { ComponentView, ComponentViewEvent, ComponentViewProperty } from './templating';

const CUSTOMIZATIONS_DIR = path.join(__dirname, 'customizations');

/**
 * Describes events that should be added to a Dash component definition.
 */
interface ComponentCustomizationEvents {
    [event: string] : {
        /**
         * If this is set, the corresponding (original) property will be updated using `setProps`.
         */
        setProperty?: string;
        /**
         * If this is set, the given property will be incremented (usually a custom property not one from the base
         * component).
         */
        incrementProperty?: string;
        /**
         * If this is set, the code (function) will simply be passed to the component.
         */
        code?: string;
    };
}

/**
 * The interface defining the schema of customization JSON objects for each component.
 */
interface ComponentCustomization {
    /**
     * A documentation string for the component.
     */
    documentation: string;
    /**
     * A list of component properties that can be persisted using Dash (e.g. `value`).
     */
    persistentProps: string[];
    /**
     * A list of additional properties to add to the component.
     */
    extraProperties: ComponentViewProperty[];
    /**
     * A list of events from the underlying component to handle.
     */
    events?: ComponentCustomizationEvents;
}

/**
 * Loads a customization JSON object from the disk.
 *
 * @param componentName The name of the component.
 * @returns The customization, or `null` if none could be found.
 */
function loadCustomization(componentName: string): ComponentCustomization | null {
    const customizationPath = path.join(CUSTOMIZATIONS_DIR, `${componentName}.json`);
    if (!fs.existsSync(customizationPath)) {
        return null;
    }

    const customization = JSON.parse(fs.readFileSync(customizationPath, 'utf-8'));
    return customization;
}

/**
 * Tries to add a new property to a list, checking if the property already exists beforehand.
 *
 * @param properties The existing properties.
 * @param property The property to add.
 * @param throwIfExists Whether an error should be thrown if the property already exists.
 * @returns The new list of properties.
 */
function tryAddProperty(properties: ComponentViewProperty[], property: ComponentViewProperty,
                        throwIfExists: boolean): ComponentViewProperty[] {
    if (properties.findIndex(p => p.name === property.name) >= 0) {
        if (throwIfExists) {
            throw new Error(`Property ${property.name} already exists.`);
        } else {
            // TODO(flo): Provide a "silent override" behavior in the future. This might be useful if we want to provide
            // access to component properties with types unsupported by Dash. We'll just replace the original property,
            // and provide some custom code for the conversion.
            return properties;
        }
    }

    return [...properties, property];
}

/**
 * Adds Dash persistence properties, which allow the state of the component to be saved.
 *
 * @param properties The existing properties.
 * @param persistedProperties The list of existing properties names that can be persisted.
 * @returns The new list of properties.
 */
function addPersistenceProperties(properties: ComponentViewProperty[],
                                  persistedProperties: string[]): ComponentViewProperty[] {
    let props = properties;

    props = tryAddProperty(props, {
        name: 'persistence',
        documentation: ['Used to allow user interactions in this component to be persisted when\n the component - or the page - is refreshed. If `persisted` is truthy and\n hasn\'t changed from its previous value, a `value` that the user has\n changed while using the app will keep that change, as long as\n the new `value` also matches what was given originally.\nUsed in conjunction with `persistence_type`.'],
        propType: 'PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number])',
        stringDefault: '',
        forwardProperty: false,
    }, true);

    const propertyList = `[${persistedProperties.map(p => `'${p}'`).join(',')}]`;
    props = tryAddProperty(props, {
        name: 'persisted_props',
        documentation: ['Properties whose user interactions will persist after refreshing the\n component or the page. Since only `value` is allowed this prop can\nnormally be ignored.'],
        propType: `PropTypes.arrayOf(PropTypes.oneOf(${propertyList}))`,
        stringDefault: propertyList,
        forwardProperty: false,
    }, true);

    props = tryAddProperty(props, {
        name: 'persistence_type',
        documentation: ['Where persisted user changes will be stored:\n memory: only kept in memory, reset on page refresh.\n local: window.localStorage, data is kept after the browser quit.\n session: window.sessionStorage, data is cleared once the browser quit.\n location: window.location, data appears in the URL and can be shared with others.'],
        propType: 'PropTypes.oneOf([\'local\', \'session\', \'memory\', \'location\'])',
        stringDefault: '\'local\'',
        forwardProperty: false,
    }, true);

    return props;
}

/**
 * Creates the list of events that will be then added to the component.
 *
 * @param events The dictionary of events to create.
 * @returns The event "views".
 */
function createEvents(events: ComponentCustomizationEvents): ComponentViewEvent[] {
    return Object.keys(events).map(event => {
        let code = '';

        if (events[event].setProperty) {
            const p = events[event].setProperty;
            code = `(e) => setProps({ ${p}: e.target.${p} })`;
        } else if (events[event].incrementProperty) {
            const p = events[event].incrementProperty;
            code = `() => setProps({ ${p}: ${p} + 1 })`
        } else if (events[event].code) {
            code = events[event].code;
        } else {
            throw new Error(`Invalid event ${event}`);
        }

        return {
            name: event,
            code,
        };
    })
}

/**
 * Transforms a component view with "manual" customization providing specificities for this component that could not be
 * inferred from its TypeScript definition.
 *
 * @param component The component to customize.
 * @return The customizes component.
 */
export function customizeComponent(component: ComponentView): ComponentView {
    let properties = component.properties;
    let events: ComponentViewEvent[] = [];

    const customization = loadCustomization(component.name);
    if (customization) {
        if (customization.persistentProps.length > 0) {
            properties = addPersistenceProperties(properties, customization.persistentProps);
        }

        customization.extraProperties.forEach(p => {
            properties = tryAddProperty(properties, p, true);
        })

        if (customization.events) {
            events = createEvents(customization.events);
        }
    }

    return {
        name: component.name,
        properties,
        events,
    }
}
