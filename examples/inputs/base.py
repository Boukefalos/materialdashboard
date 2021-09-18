from abc import ABC, abstractmethod
from dash import Dash
from dash.dependencies import Output
from dash.development.base_component import Component
from typing import List, Union


class BaseInputExample(ABC):
    """Showcases a single input component."""

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
