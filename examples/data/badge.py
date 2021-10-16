from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class BadgeDataExample(BaseExampleItem):
    """Showcases the badge component."""

    def __init__(self):
        super().__init__("badge", "Badge")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            spacing=3,
            direction="row",
            children=[
                md.Badge(
                    badgeContent=4,
                    # Can be used to hide the badge if needed.
                    invisible=False,
                    color="primary",
                    children=[md.Icon(color="action", children="mail")],
                ),
                md.Badge(
                    # Will not display a number, but simply a dot.
                    variant="dot",
                    color="secondary",
                    children=[md.Icon(color="action", children="mail")],
                ),
                md.Badge(
                    badgeContent=0,
                    # `showZero` must be `True`, otherwise `0` will be result in the badge being hidden.
                    showZero=True,
                    color="success",
                    children=[md.Icon(color="action", children="mail")],
                ),
                md.Badge(
                    badgeContent=63,
                    # Displays `50+` if the content is above `50`.
                    max=50,
                    color="primary",
                    children=[md.Icon(color="action", children="mail")],
                ),
                md.Badge(
                    badgeContent=" ",
                    color="secondary",
                    # When adding a badge on top of a circular component, setting the `overlap` ensures the badge is
                    # placed on top of the component.
                    overlap="circular",
                    # Setting `anchorOrigin` allows the badge to be placed in a different corner.
                    anchorOrigin={"vertical": "bottom", "horizontal": "right"},
                    children=[
                        md.Box(
                            component="span",
                            sx={
                                "bgcolor": "primary.main",
                                "width": 40,
                                "height": 40,
                                "borderRadius": "50%",
                            },
                        ),
                    ],
                ),
            ],
        )
