from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from .base import BaseInputExample


class SwitchInputExample(BaseInputExample):
    """Showcases how to use switches."""

    def __init__(self):
        super().__init__("switch", "Switch")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.FormGroup(
            row=True,
            children=[
                # Use a `FormControlLabel` to provide a clickable label to the switch component.
                md.FormControlLabel(
                    label="Primary color",
                    # You can choose the placement of the label around the switch.
                    labelPlacement="top",
                    children=[
                        # Like many other components, you can choose the color of the switch.
                        md.Switch(id="switch-primary", color="primary", checked=True)
                    ],
                ),
                md.FormControlLabel(
                    disabled=True,
                    label="Secondary color",
                    labelPlacement="end",
                    children=[
                        md.Switch(
                            id="switch-secondary",
                            color="secondary",
                            checked=True,
                            disabled=True,
                        )
                    ],
                ),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [Input("switch-primary", "checked")],
        )
        def on_switch_change(switch_primary_checked: str):
            return [f"Switch checked: {switch_primary_checked}"]
