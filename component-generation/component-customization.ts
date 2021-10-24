import * as fs from 'fs';
import * as path from 'path';
import {
    ComponentView,
    ComponentViewEvent,
    ComponentViewProperty,
} from './templating';

const CUSTOMIZATIONS_DIR = path.join(__dirname, 'customizations');

/**
 * Describes events that should be added to a Dash component definition.
 */
interface ComponentCustomizationEvents {
    [event: string]: {
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
 * A single custom property to add to a component.
 */
interface ComponentCustomizationProperty extends ComponentViewProperty {
    /**
     * Whether the custom property should overwrite the component property if it already exists.
     */
    overwrite?: boolean;
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
    extraProperties: ComponentCustomizationProperty[];
    /**
     * A list of events from the underlying component to handle.
     */
    events?: ComponentCustomizationEvents;
    /**
     * Extra imports that should be added at the top of the source file.
     */
    imports?: string[];
    /**
     * Additional code that should be added to the component function, before it returns the Material-UI component.
     */
    extraCode?: string[];
    /**
     * The code to insert to include children nodes in the component. Defaults to `{children}`.
     */
    childrenCode?: string;
}

/**
 * Describes a property that could not be automatically converted into a Dash component property.
 */
export interface SkippedProperty {
    /**
     * The name of the skipped property.
     */
    name: string;
    /**
     * The type of the skipped property, as a string returned by the type checked.
     */
    typeAsString: string;
    /**
     * The original documentation for the property.
     */
    documentation: string[];
    /**
     * Whether the property type is a callable (e.g. events).
     */
    isFunctionType: boolean;
}

/**
 * Loads a customization JSON object from the disk.
 *
 * @param componentName The name of the component.
 * @returns The customization, or `null` if none could be found.
 */
function loadCustomization(
    componentName: string
): ComponentCustomization | null {
    const customizationPath = path.join(
        CUSTOMIZATIONS_DIR,
        `${componentName}.json`
    );
    if (!fs.existsSync(customizationPath)) {
        return null;
    }

    const customization = JSON.parse(
        fs.readFileSync(customizationPath, 'utf-8')
    );
    return customization;
}

/**
 * Tries to add a new property to a component, checking if the property already exists beforehand.
 *
 * @param component The component to which the property should be added.
 * @param customProperty The property to add.
 * @param throwIfExists Whether an error should be thrown if the property already exists.
 * @returns `true` if the property was successfully added.
 */
function tryAddProperty(
    component: ComponentView,
    customProperty: ComponentCustomizationProperty
): boolean {
    const {overwrite, ...property} = customProperty;
    if (
        component.properties.findIndex((p) => p.name === customProperty.name) >
            0 &&
        !overwrite
    ) {
        throw new Error(`Property ${customProperty.name} already exists.`);
    }

    component.properties.push(property);
    return true;
}

/**
 * Tries to add a new event to a component, checking if the event already exists beforehand.
 *
 * @param component The component to which the event should be added.
 * @param event The event to add.
 * @param throwIfExists Whether an error should be thrown if the event already exists.
 */
function tryAddEvent(
    component: ComponentView,
    event: ComponentViewEvent,
    throwIfExists: boolean
) {
    if (component.events.findIndex((e) => e.name === event.name) >= 0) {
        if (throwIfExists) {
            throw new Error(`Event ${event.name} already exists.`);
        } else {
            return;
        }
    }

    component.events.push(event);
}

/**
 * Adds Dash persistence properties, which allow the state of the component to be saved.
 *
 * @param component The component to which the properties should be added.
 * @param persistedProperties The list of existing properties names that can be persisted.
 */
function addPersistenceProperties(
    component: ComponentView,
    persistedProperties: string[]
) {
    tryAddProperty(component, {
        name: 'persistence',
        documentation: [
            "Used to allow user interactions in this component to be persisted when\n the component - or the page - is refreshed. If `persisted` is truthy and\n hasn't changed from its previous value, a `value` that the user has\n changed while using the app will keep that change, as long as\n the new `value` also matches what was given originally.\nUsed in conjunction with `persistence_type`.",
        ],
        propType:
            'PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number])',
        stringDefault: '',
        forwardProperty: false,
    });

    const propertyList = `[${persistedProperties
        .map((p) => `'${p}'`)
        .join(',')}]`;
    tryAddProperty(component, {
        name: 'persisted_props',
        documentation: [
            'Properties whose user interactions will persist after refreshing the\n component or the page. Since only `value` is allowed this prop can\nnormally be ignored.',
        ],
        propType: `PropTypes.arrayOf(PropTypes.oneOf(${propertyList}))`,
        stringDefault: propertyList,
        forwardProperty: false,
    });

    tryAddProperty(component, {
        name: 'persistence_type',
        documentation: [
            'Where persisted user changes will be stored:\n memory: only kept in memory, reset on page refresh.\n local: window.localStorage, data is kept after the browser quit.\n session: window.sessionStorage, data is cleared once the browser quit.\n location: window.location, data appears in the URL and can be shared with others.',
        ],
        propType: "PropTypes.oneOf(['local', 'session', 'memory', 'location'])",
        stringDefault: "'local'",
        forwardProperty: false,
    });
}

/**
 * Adds base properties that should be present for all components if they do not exist already.
 *
 * @param component The component to which the properties should be added.
 * @param skippedProperties The properties that could not be converted automatically. If "base" properties are found in
 *     it, they will be added with the know PropType.
 */
function addBaseProperties(
    component: ComponentView,
    skippedProperties: SkippedProperty[]
) {
    tryAddProperty(
        component,
        {
            name: 'id',
            documentation: [
                'The ID of this component, used to identify dash components in callbacks.\nThe ID needs to be unique across all of the components in an app.',
            ],
            propType: 'PropTypes.string',
            stringDefault: '',
            forwardProperty: true,
        },
        false
    );

    const classesPropertyIndex = skippedProperties.findIndex(
        (p) => p.name === 'classes'
    );
    if (classesPropertyIndex >= 0) {
        tryAddProperty(
            component,
            {
                name: 'classes',
                documentation:
                    skippedProperties[classesPropertyIndex].documentation,
                propType: 'PropTypes.object',
                stringDefault: '',
                forwardProperty: true,
            },
            false
        );

        skippedProperties.splice(classesPropertyIndex, 1);
    }

    const stylePropertyIndex = skippedProperties.findIndex(
        (p) => p.name === 'style'
    );
    if (stylePropertyIndex >= 0) {
        tryAddProperty(
            component,
            {
                name: 'style',
                documentation:
                    skippedProperties[stylePropertyIndex].documentation,
                propType: 'PropTypes.object',
                stringDefault: '',
                forwardProperty: true,
            },
            false
        );

        skippedProperties.splice(stylePropertyIndex, 1);
    }

    const childrenPropertyIndex = skippedProperties.findIndex(
        (p) => p.name === 'children'
    );
    if (childrenPropertyIndex >= 0) {
        tryAddProperty(
            component,
            {
                name: 'children',
                documentation:
                    skippedProperties[childrenPropertyIndex].documentation,
                propType: 'PropTypes.node',
                stringDefault: '',
                forwardProperty: true,
            },
            false
        );

        skippedProperties.splice(childrenPropertyIndex, 1);
    }

    // This looks for skipped properties that accept an Element type. For those, the property is exposed as a string
    // that should be the ID of the element that will be fetched in the DOM.
    let propertyIndex = 0;
    while (propertyIndex < skippedProperties.length) {
        const currentSkippedProperty = skippedProperties[propertyIndex];
        const types = currentSkippedProperty.typeAsString.split(' | ');
        const propertyName = currentSkippedProperty.name;

        if (types.indexOf('Element') < 0) {
            propertyIndex++;
            continue;
        }

        const successfullyAdded = tryAddProperty(
            component,
            {
                name: propertyName,
                documentation: currentSkippedProperty.documentation,
                propType: 'PropTypes.string',
                stringDefault: '',
                forwardProperty: false,
            },
            false
        );

        if (!successfullyAdded) {
            propertyIndex++;
            continue;
        }

        component.extraCode.push(
            `propsToForward.${propertyName} = document.getElementById(${propertyName});`
        );

        skippedProperties.splice(propertyIndex, 1);
    }
}

/**
 * Creates the list of events that will be then added to the component.
 *
 * @param events The dictionary of events to create.
 * @returns The event "views".
 */
function createEvents(
    component: ComponentView,
    events: ComponentCustomizationEvents
) {
    Object.keys(events).forEach((event) => {
        let code = '';

        if (events[event].setProperty) {
            const p = events[event].setProperty;
            code = `(e) => setProps({ ${p}: e.target.${p} })`;
        } else if (events[event].incrementProperty) {
            const p = events[event].incrementProperty;
            code = `() => setProps({ ${p}: ${p} + 1 })`;
        } else if (events[event].code) {
            code = events[event].code;
        } else {
            throw new Error(`Invalid event ${event}`);
        }

        tryAddEvent(
            component,
            {
                name: event,
                code,
            },
            true
        );
    });
}

/**
 * Adds events that can easily be deduced from skipped properties to the given component.
 *
 * @param component The component to which events will be added.
 * @param skippedProperties The list of properties that could not be automatically converted into Dash properties. This
 *     will be searched for known properties corresponding to events.
 */
function addBaseEvents(
    component: ComponentView,
    skippedProperties: SkippedProperty[]
) {
    const onClickPropertyIndex = skippedProperties.findIndex(
        (p) => p.name === 'onClick'
    );
    if (onClickPropertyIndex >= 0) {
        tryAddProperty(component, {
            name: 'n_clicks',
            documentation: [
                'An integer that represents the number of times that this element has been clicked on.',
            ],
            propType: 'PropTypes.number',
            stringDefault: '0',
            forwardProperty: false,
        });

        tryAddEvent(
            component,
            {
                name: 'onClick',
                code: '() => setProps({ n_clicks: n_clicks + 1 })',
            },
            true
        );

        skippedProperties.splice(onClickPropertyIndex, 1);
    }

    const valuePropertyIndex = component.properties.findIndex(
        (p) => p.name === 'value'
    );
    if (valuePropertyIndex >= 0) {
        tryAddEvent(
            component,
            {
                name: 'onChange',
                code: '(e) => setProps({ value: e.target.value })',
            },
            false
        );
    }
}

/**
 * Transforms a component view with "manual" customization providing specificities for this component that could not be
 * inferred from its TypeScript definition.
 *
 * @param component The component to customize.
 * @return The customizes component.
 */
export function customizeComponent(
    component: ComponentView,
    skippedProperties: SkippedProperty[]
): void {
    const customization = loadCustomization(component.name);
    if (customization) {
        if (customization.imports) {
            component.imports = customization.imports;
        }

        if (customization.extraCode) {
            component.extraCode = customization.extraCode;
        }

        if (customization.childrenCode) {
            component.childrenCode = customization.childrenCode;
        }

        if (customization.persistentProps.length > 0) {
            addPersistenceProperties(component, customization.persistentProps);
        }

        customization.extraProperties.forEach((p) => {
            tryAddProperty(component, p);
        });

        if (customization.events) {
            createEvents(component, customization.events);
        }
    }

    addBaseProperties(component, skippedProperties);
    addBaseEvents(component, skippedProperties);
}
