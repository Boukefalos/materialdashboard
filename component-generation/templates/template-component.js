import { {{name}} as MUI{{name}} } from '@material-ui/core';
import PropTypes from 'prop-types';
import React from 'react';
{{#imports}}
{{.}}
{{/imports}}

/**
* Material-UI {{name}}.
*/
const {{name}} = (props) => {
    const {
        {{#hasChildren}}
        children,
        {{/hasChildren}}
        {{#privateProperties}}
        {{name}},
        {{/privateProperties}}
        setProps,
        ...propsToForward
    } = props;

    {{#extraCode}}
    {{.}}
    {{/extraCode}}

    return <MUI{{name}} {...propsToForward}
        {{#events}}
        {{name}}={ {{code}} }
        {{/events}}
    {{#hasChildren}}
    >
        {{childrenCode}}
    </MUI{{name}}>;
    {{/hasChildren}}
    {{^hasChildren}}
    />
    {{/hasChildren}}
}

{{name}}.defaultProps = {
    {{#propertiesWithDefault}}
    {{name}}: {{stringDefault}},
    {{/propertiesWithDefault}}
}

{{name}}.propTypes = {
    {{#properties}}
    /**
    {{#documentation}}
     * {{.}}
    {{/documentation}}
     */
    {{name}}: {{propType}},

    {{/properties}}

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
}

export default {{name}};
