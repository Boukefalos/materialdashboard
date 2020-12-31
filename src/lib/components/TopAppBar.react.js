import { AppBar, CssBaseline, IconButton, Toolbar, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import MenuIcon from '@material-ui/icons/Menu';
import PropTypes from 'prop-types';
import React from 'react';

const useStyles = makeStyles((theme) => ({
    appBar: {
        zIndex: theme.zIndex.drawer + 1
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 1
    },
}));

/**
 * An app bar at the top of the screen.
 */
const TopAppBar = (props) => {
    const classes = useStyles();

    const { children, id, n_menu_clicks, title, setProps } = props;

    return (
        <div className={classes.root}>
            <CssBaseline />

            <AppBar className={classes.appBar} id={id} position="fixed">
                <Toolbar>
                    <IconButton edge="start" color="inherit" aria-label="menu" className={classes.menuButton}
                        onClick={() => setProps({ n_menu_clicks: n_menu_clicks + 1 })}>
                        <MenuIcon />
                    </IconButton>
                    <Typography className={classes.title} variant="h6">
                        {title}
                    </Typography>

                    {children}
                </Toolbar>
            </AppBar>
        </div>
    );
}

TopAppBar.defaultProps = {
    n_menu_clicks: 0
};

TopAppBar.propTypes = {
    /**
     * Content on the right of the app bar.
     */
    children: PropTypes.node,

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Clicks made on the menu button.
     */
    n_menu_clicks: PropTypes.number,

    /**
     * A title displayed at the top of the dashboard.
     */
    title: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default TopAppBar;
