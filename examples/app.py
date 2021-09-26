import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import materialdashboard as md


DRAWER_WIDTH = "240px"
THEME = {
    "palette": {"primary": {"main": "#ff7043"}, "secondary": {"main": "#9ccc65"}},
    "zIndex": {"appBar": 1300},  # Higher than the drawer.
}


# External stylesheets contain the icons and Roboto font.
app = dash.Dash(
    __name__,
    external_stylesheets=md.external_stylesheets,
    suppress_callback_exceptions=True,
)


# The ThemeProvider allows you to set some style properties of all its children, like the color palette.
app.layout = md.ThemeProvider(
    theme=THEME,
    children=[
        html.Div(
            children=[
                # As the name suggests, adds a baseline style to the entire application.
                md.CssBaseline(),
                # The bar displayed at the top of Material applications.
                md.AppBar(
                    position="fixed",
                    className="top_bar",
                    children=[
                        md.Toolbar(
                            children=[
                                md.ButtonBase(
                                    id="menu",
                                    # edge="start",
                                    color="inherit",
                                    style={"marginRight": "10px"},
                                    children=[
                                        # Only the base Icon component is exposed. Pass the name of the icon you want to
                                        # display as the child of this component. Remember to pass the external
                                        # stylesheets when creating your web app.
                                        md.Icon(children="menu"),
                                    ],
                                ),
                                # Typography allows you to have a coherent font and size across your app. Remember to
                                # pass the external stylesheets when creating your web app.
                                md.Typography(
                                    id="title", variant="h6", children="Title"
                                ),
                            ]
                        ),
                    ],
                ),
                # The drawer allowing navigation between the app's pages. The variant used here is `persistent`, meaning
                # the drawer can be toggled and stay visible while using the rest of the app.
                md.Drawer(
                    id="drawer",
                    className="drawer",
                    classes={"paper": "drawer"},
                    variant="persistent",
                    anchor="left",
                    open=False,
                    children=[
                        # An empty toolbar adds the top offset, such that components are not hidden behind the app bar.
                        md.Toolbar(),
                        md.List(
                            children=[
                                md.ListItemButton(
                                    id="first_page",
                                    children=[md.ListItemText(primary="First page")],
                                ),
                                md.ListItemButton(
                                    id="second_page",
                                    children=[md.ListItemText(primary="Second page")],
                                ),
                            ]
                        ),
                    ],
                ),
                # Same as for the drawer.
                md.Toolbar(),
                # The main content of the app. It needs to be padded if the drawer is open.
                html.Main(
                    id="main",
                    style={"flexGrow": 1, "display": "flex"},
                    children=[
                        # The content of the container is added by `drawer_item_click()`.
                        md.Container(
                            id="main_container",
                            maxWidth=False,
                            style={"padding": "20px"},
                        ),
                    ],
                ),
            ]
        )
    ],
)


@app.callback(
    [Output("drawer", "open"), Output("main", "style")],
    [Input("menu", "n_clicks")],
    [State("drawer", "open")],
)
def drawer_button_click(n_clicks, open):
    # Toggles the drawer state.
    new_open = not open
    return (new_open, {"paddingLeft": DRAWER_WIDTH if new_open else "0"})


@app.callback(
    [Output("main_container", "children")],
    [Input("first_page", "n_clicks"), Input("second_page", "n_clicks")],
)
def drawer_item_click(*args):
    # Checks which of the two items was clicked (it could also be none if the app is initializing).
    ctx = dash.callback_context
    if ctx.triggered and ctx.triggered[0]["prop_id"].split(".")[0] == "second_page":
        return [md.Typography(children="Second page")]

    return [
        # Grid is used for both the grid itself (when `container=True`) and child elements (when `item=True`).
        md.Grid(
            style={"alignContent": "space-around", "alignItems": "center"},
            container=True,
            spacing=3,
            children=[
                md.Grid(
                    item=True,
                    md=4,
                    sm=6,
                    children=[
                        md.Typography(id="welcome", children="Welcome to my app!")
                    ],
                ),
                md.Grid(
                    item=True,
                    md=4,
                    sm=6,
                    xs=12,
                    style={"alignContent": "center"},
                    children=[
                        # Like for many other components, you can chose between several button variants. Check the
                        # Material-UI documentation for all possible options.
                        md.Button(
                            id="my_button",
                            title="Click Me!",
                            color="secondary",
                            children="Click me!",
                            variant="contained",
                        ),
                    ],
                ),
                md.Grid(
                    item=True,
                    md=4,
                    sm=6,
                    xs=12,
                    children=[
                        # A multi-function text field that you can turn into a date selector for example. Unfortunately,
                        # not all browsers are yet supported.
                        md.TextField(id="my_date_field", type="date", value=""),
                    ],
                ),
                md.Menu(
                    id="my_menu",
                    open=False,
                    children=[
                        md.MenuItem(id="option1", children="Option 1"),
                        md.MenuItem(id="option2", children="Option 2"),
                    ],
                ),
                md.Grid(
                    item=True,
                    md=4,
                    sm=6,
                    xs=12,
                    children=[
                        md.FormControl(
                            children=[
                                md.InputLabel(
                                    id="my_label",
                                    children="A label for the select",
                                ),
                                md.Select(
                                    id="my_select",
                                    style={"width": "300px"},
                                    labelId="my_label",
                                    value="test2",
                                    variant="standard",
                                    options={
                                        "test": "Option 1",
                                        "test2": "Option 2",
                                    },
                                ),
                            ]
                        ),
                    ],
                ),
                md.Grid(
                    item=True,
                    md=4,
                    sm=6,
                    xs=12,
                    children=[
                        md.Switch(id="switch", checked=True),
                    ],
                ),
            ],
        ),
    ]


@app.callback(
    [
        Output("my_menu", "open"),
        Output("my_menu", "anchorEl"),
        Output("my_button", "children"),
    ],
    [
        Input("my_button", "n_clicks"),
        Input("option1", "n_clicks"),
        Input("option2", "n_clicks"),
        Input("my_menu", "n_closes"),
    ],
)
def button_click(
    my_button_n_clicks, option1_n_clicks, option2_n_clicks, my_menu_n_closes
):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, "", dash.no_update

    clicked_item_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if clicked_item_id == "my_button":
        return True, "my_button", dash.no_update

    button_children = dash.no_update

    if clicked_item_id in ["option1", "option2"]:
        button_children = clicked_item_id

    return False, "", button_children


@app.callback(
    [
        Output("welcome", "children"),
    ],
    [
        Input("my_select", "value"),
    ],
)
def change_select(my_select_value):
    return (my_select_value,)


@app.callback(
    Output("title", "children"),
    Input("switch", "checked"),
)
def change_switch(checked):
    return "Title checked" if checked else "Title"


if __name__ == "__main__":
    app.run_server(debug=True)
