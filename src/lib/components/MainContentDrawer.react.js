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

    const {
        children,
        id,
        open,
        pages,
        selectedPage,
        setProps
    } = props;

    return (
        <>
            <CssBaseline />

            <Drawer id={id} className={classes.drawer} variant="persistent" anchor="left" open={open}
             classes={{paper: classes.drawerPaper}}>
                <Toolbar />

                <div>
                    <List>
                        {pages.map((page) => (
                            <ListItem button key={page.title} selected={page.id === selectedPage}
                                onClick={() => setProps({ selectedPage: page.id })}>
                                <ListItemText primary={page.title} />
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
};

MainContentDrawer.propTypes = {
    /**
     * The main content for the page.
     */
    children: PropTypes.node,

    /**
     * The ID of the component.
     */
    id: PropTypes.string.isRequired,

    /**
     * Whether the drawer is open.
     */
    open: PropTypes.bool,

    /**
     * The list of pages, as dictionary elements:
     * {"id": "pageId", "title": "Displayed title"}
     */
    pages: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.string.isRequired,
        title: PropTypes.string.isRequired
    })).isRequired,

    /**
     * The ID of the currently selected page.
     */
    selectedPage: PropTypes.string.isRequired,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default MainContentDrawer;
