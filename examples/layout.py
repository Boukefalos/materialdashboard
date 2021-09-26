from dash.development.base_component import Component
import materialdashboard as md

from utils import ExamplePage, run_example


class LayoutExamplePage(ExamplePage):
    """Displays a simple grid to show how elements can be laid out using the Grid component."""

    def make_layout(self) -> Component:
        # A container will limit the width of its content and center it.
        return md.Container(
            # The max width is specified as a screen size.
            maxWidth="md",
            children=[
                md.Grid(
                    style={"padding": "10px"},
                    # The container component should have the `container=True` attribute.
                    container=True,
                    # The number of columns determines the maximum sum of sizes of items in a single row.
                    # 12 is the default and doesn't need to be specified.
                    columns=12,
                    # Row and column spacing can be set independently, or the `spacing` attribute can be used to set both.
                    rowSpacing=3,
                    columnSpacing=3,
                    children=[self._make_grid_item(s) for s in [6, 3, 3, 12, 2, 10]]
                    + [
                        md.Grid(
                            item=True,
                            xs=12,
                            children=[
                                md.Stack(
                                    spacing=1,
                                    children=[
                                        self._make_paper_item(f"Stack item {i}")
                                        for i in range(1, 4)
                                    ],
                                )
                            ],
                        )
                    ],
                )
            ],
        )

    def _make_grid_item(self, size: int) -> Component:
        return md.Grid(
            # Children components should have the `item=True` attribute.
            item=True,
            # The size (in number of columns) of the item can be set depending on the screen size (xs, sm, md, lg, xl).
            # The size for each screen size can be set, or some can be left unspecified.
            # In this case, only `xs` is used, which means that the layout will always be the same, independently of the
            # screen size (hence will be unresponsive).
            xs=size,
            children=[self._make_paper_item(f"Size {size}")],
        )

    def _make_paper_item(self, text: str) -> md.Paper:
        return md.Paper(
            children=[text],
            style={
                "padding": "20px",
                "textAlign": "center",
                "backgroundColor": "#eeeeee",
            },
        )


if __name__ == "__main__":
    run_example(LayoutExamplePage)
