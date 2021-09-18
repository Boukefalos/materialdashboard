from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from .base import BaseInputExample


class SliderInputExample(BaseInputExample):
    """Showcases how to use sliders."""

    def __init__(self):
        super().__init__("slider", "Slider")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Box(
            style={"width": "200px"},
            children=[
                md.Slider(
                    id="slider-default",
                    # Will display a label when the slider is being edited, but it can also be always `on`.
                    valueLabelDisplay="auto",
                    min=5,
                    max=40,
                    value=35,
                    # You can set marks that will be displayed along the slider.
                    marks=[
                        {"value": 10, "label": "⚠️ 10"},
                        {"value": 25, "label": "✅ 25"},
                    ],
                ),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback([feedback_output], [Input("slider-default", "value")])
        def on_slider_change(slider_default: float):
            return [f"Slider value is {slider_default}"]
