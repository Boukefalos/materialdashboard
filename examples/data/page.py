from data.badge import BadgeDataExample
from data.chip import ChipDataExample
from data.list import ListDataExample
from data.table import TableDataExample
from data.typography import TypographyDataExample
from utils import ListExamplePage, run_example

from .avatar import AvatarDataExample


class DataExamplePage(ListExamplePage):
    """Showcases various data components."""

    def __init__(self):
        super().__init__(
            [
                AvatarDataExample(),
                BadgeDataExample(),
                ChipDataExample(),
                ListDataExample(),
                TableDataExample(),
                TypographyDataExample(),
            ]
        )


if __name__ == "__main__":
    run_example(DataExamplePage)
