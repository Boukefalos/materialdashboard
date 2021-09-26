from abc import ABC, abstractmethod
from dash import Dash
from dash.development.base_component import Component
import dash_html_components as html
import materialdashboard as md
from typing import Type


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
