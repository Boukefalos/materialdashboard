import dash
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class ListDataExample(BaseExampleItem):
    """Showcases the list component."""

    def __init__(self):
        super().__init__("list", "List")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Grid(
            container=True,
            spacing=2,
            direction="row",
            children=[
                md.Grid(item=True, children=c, xl=4)
                for c in [
                    self.make_list_with_buttons_layout(),
                    self.make_list_with_headers_layout(),
                ]
            ],
        )

    def make_list_with_buttons_layout(self) -> Component:
        """Creates a list using list buttons, icons, and dividers."""
        return (
            md.Box(
                sx={
                    "width": "100%",
                    "maxWidth": 360,
                    "bgcolor": "background.paper",
                },
                children=[
                    md.List(
                        children=[
                            md.ListItem(
                                # The list item will be highlighted if marked as `selected`.
                                selected=item[3],
                                disablePadding=True,
                                children=[
                                    # Using a `ListItemButton` will implement the usual clicking behavior.
                                    md.ListItemButton(
                                        id=f"list-button-{item[0]}",
                                        children=[
                                            # An icon can be displayed before the main text using `ListItemIcon`.
                                            md.ListItemIcon(
                                                children=[
                                                    md.Icon(children=item[0]),
                                                ]
                                            ),
                                            md.ListItemText(
                                                primary=item[1],
                                                # An optional secondary line can be displayed with smaller text.
                                                secondary=item[2],
                                            ),
                                        ],
                                    ),
                                ],
                            )
                            for item in [
                                ("inbox", "Inbox", "39 unread", False),
                                ("drafts", "Drafts", None, True),
                            ]
                        ]
                    ),
                    md.Divider(),
                    md.List(
                        children=[
                            md.ListItem(
                                disablePadding=True,
                                children=[
                                    md.ListItemButton(
                                        id=f"list-button-{text.lower()}",
                                        children=[
                                            md.ListItemText(primary=text),
                                        ],
                                    ),
                                ],
                            )
                            for text in ["Trash", "Spam"]
                        ]
                    ),
                ],
            ),
        )

    def make_list_with_headers_layout(self) -> Component:
        """Creates a list with sticky headers and avatars."""
        return md.List(
            sx={
                "width": "100%",
                "maxWidth": 360,
                "bgcolor": "background.paper",
                "position": "relative",
                "overflow": "auto",
                "maxHeight": 300,
                "padding": 0,
                "& ul": {"padding": 0},
            },
            children=[
                html.Li(
                    key=f"section={section}",
                    children=[
                        html.Ul(
                            children=[
                                # `ListSubheader` shows a sticky header for a section in the list.
                                md.ListSubheader(children=f"I'm sticky {section}")
                            ]
                            + [
                                md.ListItem(
                                    key=f"item-{section}-{item}",
                                    children=[
                                        # Instead of an icon, an avatar can also be shown next to the item's text.
                                        md.ListItemAvatar(
                                            children=md.Avatar(
                                                children=md.Icon(children="backup")
                                            )
                                        ),
                                        md.ListItemText(primary=f"Item {item}"),
                                    ],
                                )
                                for item in range(3)
                            ],
                        )
                    ],
                )
                for section in range(5)
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            feedback_output,
            [
                Input("list-button-inbox", "n_clicks"),
                Input("list-button-drafts", "n_clicks"),
                Input("list-button-trash", "n_clicks"),
                Input("list-button-spam", "n_clicks"),
            ],
        )
        def on_list_button_click(*args):
            ctx = dash.callback_context

            if ctx.triggered:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]
                button_name = button_id.split("-")[-1]
                return f"You clicked {button_name}!"

            return ""
