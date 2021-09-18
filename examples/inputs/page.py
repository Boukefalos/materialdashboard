from inputs.toggle import ToggleButtonInputExample
from inputs.textfield import TextFieldInputExample
from inputs.switch import SwitchInputExample
from inputs.slider import SliderInputExample
from inputs.select import SelectInputExample
from inputs.rating import RatingInputExample
from inputs.radio import RadioButtonInputExample
from inputs.fab import FloatingActionButtonInputExample
from inputs.checkbox import CheckboxInputExample
from dash import Dash
from typing import List
from dash.dependencies import Output
from dash.development.base_component import Component
import materialdashboard as md

from utils import ExamplePage, run_example

from .base import BaseInputExample
from .button import ButtonInputExample


class InputsExamplePage(ExamplePage):
    """Showcases various input components."""

    def __init__(self):
        super().__init__()

        self._examples = [
            ButtonInputExample(),
            CheckboxInputExample(),
            FloatingActionButtonInputExample(),
            RadioButtonInputExample(),
            RatingInputExample(),
            SelectInputExample(),
            SliderInputExample(),
            SwitchInputExample(),
            TextFieldInputExample(),
            ToggleButtonInputExample(),
        ]

    def make_layout(self) -> Component:
        return md.Container(
            children=[
                md.Grid(
                    container=True,
                    spacing=4,
                    children=[
                        item
                        for example in self._examples
                        for item in self._make_grid_item(example)
                    ],
                )
            ]
        )

    def _make_grid_item(
        self,
        example: BaseInputExample,
    ) -> List[md.Grid]:
        return [
            md.Grid(
                item=True,
                xs=12,
                sm=12,
                md=2,
                style={"display": "flex", "alignItems": "center"},
                children=example.display_name,
            ),
            md.Grid(
                item=True,
                xs=8,
                sm=8,
                md=8,
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                },
                children=example.make_layout(),
            ),
            md.Grid(
                id=f"{example.id_prefix}-feedback",
                item=True,
                xs=4,
                sm=4,
                md=2,
                style={"display": "flex", "alignItems": "center"},
            ),
        ]

    def register_callbacks(self, app: Dash):
        for example in self._examples:
            output = Output(f"{example.id_prefix}-feedback", "children")
            example.register_callbacks(app, output)


if __name__ == "__main__":
    run_example(InputsExamplePage)
