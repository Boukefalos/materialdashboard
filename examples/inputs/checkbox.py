from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class CheckboxInputExample(BaseExampleItem):
    """Showcases how to use checkboxes."""

    def __init__(self):
        super().__init__("checkbox", "Checkbox")

    def make_layout(self) -> Union[Component, List[Component]]:
        # Simply use the `checked` property to set or get notified of changes to the checkbox state.
        # When `True`, `disabled` grays out the component.
        return [
            md.Checkbox(id="checkbox-1", checked=True),
            md.Checkbox(id="checkbox-2", checked=False),
            md.Checkbox(disabled=True),
            md.Checkbox(disabled=True, checked=True),
        ]

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [
                Input("checkbox-1", "checked"),
                Input("checkbox-2", "checked"),
            ],
        )
        def on_checkbox_click(checkbox1_checked: bool, checkbox2_checked: bool):
            return [f"Checkbox 1: {checkbox1_checked}, Checkbox 2: {checkbox2_checked}"]
