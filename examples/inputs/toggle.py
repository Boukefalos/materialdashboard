from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class ToggleButtonInputExample(BaseExampleItem):
    """Showcases how to use toggle buttons."""

    def __init__(self):
        super().__init__("toggle-button", "Toggle Button")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            direction="row",
            spacing=2,
            children=[
                # Toggle buttons can be used individually, somewhat similarly to checkboxes.
                md.ToggleButton(
                    id="toggle-button-single",
                    selected=True,
                    children=[md.Icon(children="check")],
                ),
                # A `ToggleButtonGroup` is a more relevant usecase, where one or several buttons can be selected within
                # a group.
                md.ToggleButtonGroup(
                    id="toggle-button-group",
                    # When `exclusive` is `False`, several buttons can be selected at the same time.
                    exclusive=False,
                    # If `exclusive` is `False`, `value` should be a list and not a single value.
                    value=["left"],
                    # The list of buttons to display, as a dictionary of `{"value": "icon name"}`.
                    buttons={
                        "left": "format_align_left",
                        "center": "format_align_center",
                        "right": "format_align_right",
                        "justify": "format_align_justify",
                    },
                ),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [
                Input("toggle-button-single", "selected"),
                Input("toggle-button-group", "value"),
            ],
        )
        def on_toggle_button_changed(
            toggle_button_single: bool, toggle_button_group_value: List[str]
        ):
            return [
                f"Single button selected: {toggle_button_single}, in group: {toggle_button_group_value}"
            ]
