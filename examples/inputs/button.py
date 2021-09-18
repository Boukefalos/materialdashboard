import dash
from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from .base import BaseInputExample


class ButtonInputExample(BaseInputExample):
    """Showcases how the button component can be used with various styles."""

    def __init__(self):
        super().__init__("button", "Button")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            spacing=2,
            direction="row",
            children=[
                md.Button(id="button-text", children="Text", variant="text"),
                md.Button(
                    id="button-contained", children="Contained", variant="contained"
                ),
                md.Button(
                    id="button-outlined", children="Outlined", variant="outlined"
                ),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        # Just like many other Dash components, you can use the `n_clicks` property to get notified of clicks on the
        # buttons.
        @app.callback(
            feedback_output,
            [
                Input("button-text", "n_clicks"),
                Input("button-contained", "n_clicks"),
                Input("button-outlined", "n_clicks"),
            ],
        )
        def on_button_click(*args):
            ctx = dash.callback_context

            if ctx.triggered:
                button_id = ctx.triggered[0]["prop_id"].split(".")[0]
                button_name = button_id.split("-")[1]
                return f"You clicked {button_name}!"

            return ""
