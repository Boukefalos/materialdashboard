import clsx from 'clsx';
import {
    CssBaseline,
    Drawer,
    List,
    ListItem,
    ListItemText,
    Toolbar,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import React from 'react';

const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
    },
    drawerPaper: {
        width: drawerWidth,
    },
    content: {
        flexGrow: 1,
        padding: theme.spacing(3),
        transition: theme.transitions.create('margin', {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        marginLeft: -drawerWidth,
    },
    contentShift: {
        transition: theme.transitions.create('margin', {
            easing: theme.transitions.easing.easeOut,
            duration: theme.transitions.duration.enteringScreen,
        }),
        marginLeft: 0,
    },
}));

/**
 * A component adding a drawer and nesting the main page content.
 */
const MainContentDrawer = (props) => {
    const classes = useStyles();

    const { children, id, open, pages, value, setProps } = props;

    return (
        <>
            <CssBaseline />

            <Drawer id={id} className={classes.drawer} variant="persistent" anchor="left" open={open}
             classes={{paper: classes.drawerPaper}}>
                <Toolbar />

                <div>
                    <List>
                        {pages.map((page) => (
                            <ListItem button key={page.value} selected={page.value === value}
                                onClick={() => setProps({ value: page.value })}>
                                <ListItemText primary={page.label} />
                            </ListItem>
                        ))}
                    </List>
                </div>
            </Drawer>

            <main className={clsx(classes.content, { [classes.contentShift]: open })}>
                <Toolbar />

                {children}
            </main>
        </>
    );
}

MainContentDrawer.defaultProps = {
    open: true,
    persisted_props: ['value'],
    persistence_type: 'local',
};

MainContentDrawer.propTypes = {
    /**
     * The main content for the page.
     */
    children: PropTypes.node,

    /**
     * The ID of the component.
     */
    id: PropTypes.string,

    /**
     * Whether the drawer is open.
     */
    open: PropTypes.bool,

    /**
     * The list of pages, as dictionary elements:
     * {"value": "pageId", "label": "Displayed title"}
     */
    pages: PropTypes.arrayOf(PropTypes.shape({
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
     * The ID of the currently selected page.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default MainContentDrawer;
