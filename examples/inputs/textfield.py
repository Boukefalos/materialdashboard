from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class TextFieldInputExample(BaseExampleItem):
    """Showcases how to use text fields."""

    def __init__(self):
        super().__init__("text-field", "Text Field")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            spacing=1,
            direction="row",
            children=[
                md.TextField(id="text-field-default", label="Label", value="default"),
                # Several properties are common across components: `variant`, `error`.
                md.TextField(
                    id="text-field-password",
                    label="Standard variant",
                    value="default",
                    # You can set the type of text field.
                    type="password",
                    error=True,
                    variant="standard",
                    # Will be displayed below the text field.
                    helperText="Invalid password",
                ),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [
                Input("text-field-default", "value"),
                Input("text-field-password", "value"),
            ],
        )
        def on_text_field_change(text_field_default: str, text_field_password: str):
            return [
                f"First field is {text_field_default}, password is {text_field_password}."
            ]
