import dash
from dash import Dash
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class ChipDataExample(BaseExampleItem):
    """Showcases the chip component."""

    def __init__(self):
        super().__init__("chip", "Chip")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Grid(
            container=True,
            spacing=2,
            direction="row",
            children=[
                md.Grid(item=True, children=c, xl=4)
                for c in [
                    md.Chip(label="Filled", color="success"),
                    md.Chip(
                        id="chip-clickable",
                        label="Outlined and clickable",
                        variant="outlined",
                        # When `clickable`, the `n_clicks` property is incremented on each click.
                        clickable=True,
                        color="primary",
                    ),
                    md.Chip(
                        id="chip-deletable",
                        label="Deletable",
                        # When `deleteIcon` is anything but `False`, the `n_deletes` property is incremented on each
                        # click on the delete button.
                        deleteIcon=True,
                    ),
                    md.Chip(
                        id="chip-clickable_deletable",
                        label="Clickable and deletable",
                        # A chip can be both clickable on its entire body and on the delete icon.
                        clickable=True,
                        # When the `deleteIcon` is a string, it is interpreted as the name of the icon to show.
                        deleteIcon="done",
                    ),
                    md.Chip(
                        label="With Icon",
                        # The name of the icon that will be displayed in the body.
                        icon="face",
                    ),
                    md.Chip(
                        label="Avatar",
                        # Instead of an icon, an avatar can be displayed with either an image (using `src`)...
                        avatar={"src": "default"},
                    ),
                    md.Chip(
                        label="Avatar",
                        # ... or "initials" (using `children`).
                        avatar={"children": "FV"},
                    ),
                ]
            ],
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        @app.callback(
            feedback_output,
            [
                Input("chip-clickable", "n_clicks"),
                Input("chip-deletable", "n_deletes"),
                Input("chip-clickable_deletable", "n_clicks"),
                Input("chip-clickable_deletable", "n_deletes"),
            ],
        )
        def on_chip_click(*args):
            ctx = dash.callback_context

            if ctx.triggered:
                chip_id, chip_property = ctx.triggered[0]["prop_id"].split(".")
                chip_name = chip_id.split("-")[1]
                action = "clicked" if chip_property == "n_clicks" else "deleted"
                return f"You {action} {chip_name}!"

            return ""
