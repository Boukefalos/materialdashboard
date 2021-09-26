from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from .base import BaseInputExample


class RatingInputExample(BaseInputExample):
    """Showcases how to use ratings."""

    def __init__(self):
        super().__init__("rating", "Rating")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            spacing=1,
            children=[
                md.Typography(component="legend", children="Active"),
                md.Rating(
                    id="rating",
                    value=3.5,
                    # The default precision allows increments of 1 star, but you can set a finer scale.
                    precision=0.5,
                ),
                md.Typography(component="legend", children="Disabled"),
                md.Rating(name="disabled", value=3, disabled=True),
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            [feedback_output],
            [Input("rating", "value")],
        )
        def on_rating_change(value: float):
            return [f"You rated {value}."]
