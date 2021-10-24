import dash
from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class FloatingActionButtonInputExample(BaseExampleItem):
    """Showcases how to use floating action buttons."""

    def __init__(self):
        super().__init__("floating-action-button", "Floating Action Button")

    def make_layout(self) -> Union[Component, List[Component]]:
        # Just like regular buttons, you can set the color of the component. `primary` and `secondary` refer to the
        # theme's colors.
        return md.Stack(
            spacing=2,
            direction="row",
            children=[
                md.Fab(
                    id="fab-primary",
                    color="primary",
                    children=md.Icon(children="add"),
                ),
                md.Fab(
                    id="fab-secondary",
                    color="secondary",
                    children=md.Icon(children="edit"),
                ),
                # The extended variant allows a non-round button.
                md.Fab(
                    id="fab-extended",
                    variant="extended",
                    children=[
                        md.Icon(children="navigation"),
                        "Navigate",
                    ],
                ),
                md.Fab(
                    disabled=True,
                    children=md.Icon(children="favorite"),
                ),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [
                Input("fab-primary", "n_clicks"),
                Input("fab-secondary", "n_clicks"),
                Input("fab-extended", "n_clicks"),
            ],
        )
        def on_fab_click(*args):
            ctx = dash.callback_context

            if ctx.triggered:
                button_name = ctx.triggered[0]["prop_id"].split(".")[0].split("-")[1]
                return [f"You clicked {button_name}!"]

            return [""]
