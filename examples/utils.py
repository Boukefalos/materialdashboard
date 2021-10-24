from abc import ABC, abstractmethod
from dash import Dash
from dash.dependencies import Output
from dash.development.base_component import Component
import dash_html_components as html
import materialdashboard as md
from typing import List, Type, Union


class ExamplePage(ABC):
    """An base example page that should be subclassed to present `materialdashboard` capabilities."""

    @abstractmethod
    def make_layout(self) -> Component:
        """Makes the layout for the page.

        Returns:
            The root component for the layout."""
        pass

    def register_callbacks(self, app: Dash):
        """Called after the layout has been set and should be used to register callbacks on the inputs.

        Args:
            app (Dash): The Dash app that can be used to register callbacks."""
        pass


class BaseExampleItem(ABC):
    """Showcases a single component."""

    def __init__(self, id_prefix: str, display_name: str):
        """Initializes a new example.

        Args:
            id_prefix (str): The unique prefix for IDs, e.g. the feedback component.
            display_name (str): The name of the component that will be displayed to the user.
        """
        self.id_prefix = id_prefix
        self.display_name = display_name

    @abstractmethod
    def make_layout(self) -> Union[Component, List[Component]]:
        """Generates the components for this example.

        Returns:
            The components.
        """
        return []

    def register_callbacks(self, app: Dash, feedback_output: Output):
        """Registers callbacks for this example.

        Args:
            app (Dash): The parent dash app.
            feedback_output (Output): The output in which user feedback can be displayed.
        """
        pass


class ListExamplePage(ExamplePage):
    """A page showing a list of components."""

    def __init__(self, examples: List[BaseExampleItem]):
        """Creates a new page showing several items.

        Args:
            examples: The list of example items to show.
        """
        super().__init__()

        self._examples = examples

    def make_layout(self) -> Component:
        return md.Container(
            style={"padding": "20px"},
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
            ],
        )

    def _make_grid_item(
        self,
        example: BaseExampleItem,
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


def run_example(PageClass: Type[ExamplePage]):
    """Starts the server and presents an example page.

    Args:
        PageClass (Type[ExamplePage]): The class for the page to present.
    """
    page = PageClass()
    app = Dash(
        __name__,
        external_stylesheets=md.external_stylesheets,
    )
    app.layout = html.Div(children=[md.CssBaseline(), page.make_layout()])
    page.register_callbacks(app)
    app.run_server(debug=True)
