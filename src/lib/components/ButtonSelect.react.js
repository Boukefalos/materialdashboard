import {
    Button,
    Menu,
    MenuItem
} from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import PropTypes from 'prop-types';
import React, { useState } from 'react';

/**
 * A select component made from a material button.
 */
const ButtonSelect = (props) => {
    const [ anchorEl, setAnchorEl ] = useState()
    const { open, options, selectedOption, setProps } = props;

    return (
        <>
            <Button color="inherit" onClick={(e) => {
                setAnchorEl(e.currentTarget);
                setProps({ open: true });
            }}>
                {options.find((o) => o.value === selectedOption).text}
                <ExpandMoreIcon fontSize="small" />
            </Button>
            <Menu open={open} anchorEl={anchorEl} onClose={() => setProps({ open: false })}>
                {options.map((option) => (
                    <MenuItem value={option.value} selected={option.value === selectedOption}
                     onClick={() => setProps({ open: false, selectedOption: option.value})}>
                        {option.text}
                    </MenuItem>
                ))}
            </Menu>
        </>
    );
}

ButtonSelect.defaultProps = {
    open: false,
}

ButtonSelect.propTypes = {
    /**
     * Whether the select menu is open.
     */
    open: PropTypes.bool,

    /**
     * The list of available options in the select menu, as dictionary elements:
     * {"value": "optionId", "text": "Displayed option"}
     */
    options: PropTypes.arrayOf(PropTypes.shape({
        value: PropTypes.string.isRequired,
        text: PropTypes.string.isRequired
    })).isRequired,

    /**
     * The value (ID) of the currently selected option.
     */
    selectedOption: PropTypes.string.isRequired,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
}

export default ButtonSelect;
