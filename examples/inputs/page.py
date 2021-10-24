from utils import ListExamplePage, run_example

from .button import ButtonInputExample
from .checkbox import CheckboxInputExample
from .fab import FloatingActionButtonInputExample
from .radio import RadioButtonInputExample
from .rating import RatingInputExample
from .select import SelectInputExample
from .slider import SliderInputExample
from .switch import SwitchInputExample
from .textfield import TextFieldInputExample
from .toggle import ToggleButtonInputExample


class InputsExamplePage(ListExamplePage):
    """Showcases various input components."""

    def __init__(self):
        super().__init__(
            [
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
        )


if __name__ == "__main__":
    run_example(InputsExamplePage)
