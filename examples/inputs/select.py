from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from .base import BaseInputExample


class SelectInputExample(BaseInputExample):
    """Showcases how to use selects."""

    def __init__(self):
        super().__init__("select", "Select")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            spacing=1,
            children=md.Stack(
                spacing=1,
                direction="row",
                children=[
                    md.FormControl(
                        # You can define the `variant` at the `FormControl` level.
                        variant="outlined",
                        fullWidth=True,
                        children=[
                            # Defines a label for the select.
                            md.InputLabel(
                                id="outlined-select-label", children="Outlined"
                            ),
                            md.Select(
                                id="select-outlined",
                                labelId="outlined-select-label",
                                # The label should be redefined here.
                                label="Outlined",
                                # Setting a value of `""` will select no option.
                                value="",
                                # Set the options as a dictionary of `{"value": "label"}`.
                                options={
                                    "10": "Ten",
                                    "20": "Twenty",
                                },
                            ),
                            # Will be displayed right below the select component.
                            md.FormHelperText(children="You should pick something."),
                        ],
                    ),
                    md.FormControl(
                        variant="filled",
                        # You can set the control to be in an error state to request changes to the user.
                        error=True,
                        fullWidth=True,
                        children=[
                            md.InputLabel(
                                id="filled-select-label", children="Filled, with error"
                            ),
                            md.Select(
                                id="select-filled",
                                labelId="filled-select-label",
                                label="Filled, with error",
                                value="20",
                                options={
                                    "10": "Ten",
                                    "20": "Twenty",
                                },
                            ),
                            md.FormHelperText(children="Please select something else."),
                        ],
                    ),
                ],
            ),
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [Input("select-outlined", "value"), Input("select-filled", "value")],
        )
        def on_select_change(select_outlined_value: str, select_filled_value: str):
            return [
                f"You selected {select_outlined_value if len(select_outlined_value) else '<empty>'} "
                f"and {select_filled_value}."
            ]
