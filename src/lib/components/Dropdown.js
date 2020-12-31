import {
    Button,
    Menu,
    MenuItem
} from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import PropTypes from 'prop-types';
import React, { useState } from 'react';

/**
 * A dropdown component made from a material button.
 */
const Dropdown = (props) => {
    const [ anchorEl, setAnchorEl ] = useState()
    const { id, open, options: rawOptions, value, setProps } = props;

    const options = rawOptions || [];
    const selectedOption = options.find((o) => o.value === value);

    return (
        <>
            <Button id={id} color="inherit" onClick={(e) => {
                setAnchorEl(e.currentTarget);
                setProps({ open: true });
            }}>
                {selectedOption ? selectedOption.label : ''}
                <ExpandMoreIcon fontSize="small" />
            </Button>
            <Menu open={open} anchorEl={anchorEl} onClose={() => setProps({ open: false })}>
                {options.map((option) => (
                    <MenuItem key={option.value} value={option.value} selected={option.value === value}
                     onClick={() => setProps({ open: false, value: option.value})}>
                        {option.label}
                    </MenuItem>
                ))}
            </Menu>
        </>
    );
}

Dropdown.defaultProps = {
    open: false,
    persisted_props: ['value'],
    persistence_type: 'local',
}

Dropdown.propTypes = {
    /**
     * The ID of this component, used to identify dash components in callbacks.
     * The ID needs to be unique across all of the components in an app.
     */
    id: PropTypes.string,

    /**
     * Whether the dropdown menu is open.
     */
    open: PropTypes.bool,

    /**
     * The list of available options in the select menu, as dictionary elements:
     * {"value": "optionId", "label": "Displayed option"}
     */
    options: PropTypes.arrayOf(PropTypes.shape({
        value: PropTypes.string.isRequired,
        label: PropTypes.string.isRequired
    })),

    /**
     * Used to allow user interactions in this component to be persisted when
     * the component - or the page - is refreshed. If `persisted` is truthy and
     * hasn't changed from its previous value, a `value` that the user has
     * changed while using the app will keep that change, as long as
     * the new `value` also matches what was given originally.
     * Used in conjunction with `persistence_type`.
     */
    persistence: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.string,
        PropTypes.number,
    ]),

    /**
     * Properties whose user interactions will persist after refreshing the
     * component or the page. Since only `value` is allowed this prop can
     * normally be ignored.
     */
    persisted_props: PropTypes.arrayOf(PropTypes.oneOf(['value'])),

    /**
     * Where persisted user changes will be stored:
     * memory: only kept in memory, reset on page refresh.
     * local: window.localStorage, data is kept after the browser quit.
     * session: window.sessionStorage, data is cleared once the browser quit.
     * location: window.location, data appears in the URL and can be shared with others.
     */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory', 'location']),

    /**
     * The value (ID) of the currently selected option.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
}

export default Dropdown;
