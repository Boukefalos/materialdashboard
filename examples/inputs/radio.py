from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class RadioButtonInputExample(BaseExampleItem):
    """Showcases how to use radio buttons."""

    def __init__(self):
        super().__init__("radio-button", "Radio Button")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.FormControl(
            # This determines the type of HTML component used by `FormControl`.
            component="fieldset",
            children=[
                # A label can be used to add a legend to the list of options.
                md.FormLabel(component="legend", children="Gender"),
                # You should group radio buttons in a `RadioGroup` component.
                # You will watch the `value` of this component, rather the individual radio buttons.
                md.RadioGroup(
                    id="radio-group",
                    row=True,  # Determines how the options are displayed.
                    name="radio-group",
                    value="female",
                    children=[
                        # Wrap each `Radio` component in a `FormControlLabel` to add a label to it.
                        # Note that the original `control` property of the `FormControlLabel` translates to the
                        # `children` property.
                        md.FormControlLabel(
                            value="female",
                            label="Female",
                            # A caveat of using Dash is that you should manually propagate properties set on the
                            # `FormControlLabel` to the child `Radio` component. The `FormControlLabel` usually takes
                            # case of this, but Dash overrides the properties of the child.
                            children=[md.Radio(value="female")],
                        ),
                        md.FormControlLabel(
                            value="male",
                            label="Male",
                            children=[md.Radio(value="male")],
                        ),
                        md.FormControlLabel(
                            value="other",
                            label="Other",
                            children=[md.Radio(value="other")],
                        ),
                        md.FormControlLabel(
                            disabled=True,
                            value="disabled",
                            label="Not active",
                            # Same as above, you need to manually forward the `disabled` property.
                            children=[md.Radio(disabled=True)],
                        ),
                    ],
                ),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [Input("radio-group", "value")],
        )
        def on_radio_change(value: str):
            return [f"You selected {value}."]
