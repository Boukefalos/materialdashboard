from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class TypographyDataExample(BaseExampleItem):
    """Showcases the typography component."""

    def __init__(self):
        super().__init__("typography", "Typography")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Box(
            sx={"width": "100%", "maxWidth": 500},
            children=[
                md.Typography(
                    # The "style" of this block, which could be a title or a paragraph for example.
                    variant="h1",
                    # The HTML component to use to display the block.
                    component="div",
                    # Adds a bottom margin.
                    gutterBottom=True,
                    children="h1. Heading",
                ),
                md.Typography(
                    variant="h2",
                    gutterBottom=True,
                    component="div",
                    children="h2. Heading",
                ),
                md.Typography(
                    variant="h3",
                    gutterBottom=True,
                    component="div",
                    children="h3. Heading",
                ),
                md.Typography(
                    variant="h4",
                    gutterBottom=True,
                    component="div",
                    children="h4. Heading",
                ),
                md.Typography(
                    variant="h5",
                    gutterBottom=True,
                    component="div",
                    children="h5. Heading",
                ),
                md.Typography(
                    variant="h6",
                    gutterBottom=True,
                    component="div",
                    children="h6. Heading",
                ),
                md.Typography(
                    variant="subtitle1",
                    gutterBottom=True,
                    component="div",
                    children="subtitle1. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos blanditiis tenetur",
                ),
                md.Typography(
                    variant="subtitle2",
                    gutterBottom=True,
                    component="div",
                    children="subtitle2. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos blanditiis tenetur",
                ),
                md.Typography(
                    variant="body1",
                    gutterBottom=True,
                    children="body1. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos blanditiis tenetur unde suscipit, quam beatae rerum inventore consectetur, neque doloribus, cupiditate numquam dignissimos laborum fugiat deleniti? Eum quasi quidem quibusdam.",
                ),
                md.Typography(
                    variant="body2",
                    gutterBottom=True,
                    children="body2. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos blanditiis tenetur unde suscipit, quam beatae rerum inventore consectetur, neque doloribus, cupiditate numquam dignissimos laborum fugiat deleniti? Eum quasi quidem quibusdam.",
                ),
                md.Typography(
                    variant="button",
                    display="block",
                    gutterBottom=True,
                    children="button text",
                ),
                md.Typography(
                    variant="caption",
                    display="block",
                    gutterBottom=True,
                    children="caption text",
                ),
                md.Typography(
                    variant="overline",
                    display="block",
                    gutterBottom=True,
                    children="overline text",
                ),
            ],
        )
