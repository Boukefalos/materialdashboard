from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Union

from utils import BaseExampleItem


class AvatarDataExample(BaseExampleItem):
    """Showcases the avatar component."""

    def __init__(self):
        super().__init__("avatar", "Avatar")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            spacing=2,
            direction="row",
            children=[
                # An avatar group will cap the maximum number of avatars displayed.
                md.AvatarGroup(
                    max=3,
                    children=[
                        # Use the `sx` property to change the appearance, e.g. the background colour.
                        md.Avatar(children="FV", sx={"bgcolor": "#3368FF"}),
                        md.Avatar(children="AB", sx={"bgcolor": "#FF5733"}),
                        md.Avatar(children="CD"),
                        md.Avatar(children="EF"),
                    ],
                ),
                # An avatar can also show an icon.
                md.Avatar(children=[md.Icon(children="assignment")]),
                # To add a badge to the avatar, make sure to set the `overlap` to `circular`.
                md.Badge(
                    color="primary",
                    badgeContent="5",
                    overlap="circular",
                    # To display an image, use the `src` property. If the image is not found, a default silhouette will
                    # be shown.
                    children=md.Avatar(src="oops"),
                ),
            ],
        )
