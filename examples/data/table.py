import dash
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.development.base_component import Component
import materialdashboard as md
from typing import List, Tuple, Union

from utils import BaseExampleItem


TABLE_COLUMNS = [
    "Dessert (100g serving)",
    "Calories",
    "Fat (g)",
    "Carbs (g)",
    "Protein (g)",
]
TABLE_ROWS = [
    ("Cupcake", 305, 3.7, 67, 4.3),
    ("Donut", 452, 25.0, 51, 4.9),
    ("Eclair", 262, 16.0, 24, 6.0),
    ("Frozen yoghurt", 159, 6.0, 24, 4.0),
    ("Gingerbread", 356, 16.0, 49, 3.9),
    ("Honeycomb", 408, 3.2, 87, 6.5),
    ("Ice cream sandwich", 237, 9.0, 37, 4.3),
    ("Jelly Bean", 375, 0.0, 94, 0.0),
    ("KitKat", 518, 26.0, 65, 7.0),
    ("Lollipop", 392, 0.2, 98, 0.0),
    ("Marshmallow", 318, 0, 81, 2.0),
    ("Nougat", 360, 19.0, 9, 37.0),
    ("Oreo", 437, 18.0, 63, 4.0),
]


class TableDataExample(BaseExampleItem):
    """Showcases the table component."""

    def __init__(self):
        super().__init__("table", "Table")

    def make_layout(self) -> Union[Component, List[Component]]:
        return md.Stack(
            spacing=3,
            direction="row",
            children=[
                md.Paper(
                    sx={"width": "100%", "overflow": "hidden"},
                    children=[
                        md.TableContainer(
                            # The maximum height is used in the example to showcase sticky headers.
                            sx={"maxHeight": 300},
                            children=[
                                md.Table(
                                    # When `small`, a "dense" table is displayed.
                                    size="medium",
                                    # The headers will stay on top when scrolling.
                                    stickyHeader=True,
                                    sx={"minWidth": 650},
                                    children=[
                                        self._make_table_head(),
                                        md.TableBody(id="table-body"),
                                    ],
                                )
                            ],
                        ),
                        # `TablePagination` adds controls to navigate through pages. It is used outside the table to
                        # prevent scrolling, but could also be added in the table footer.
                        md.TablePagination(
                            id="table-pagination",
                            # The options made available to the user through a drop down.
                            rowsPerPageOptions=[2, 5, 10],
                            component="div",
                            # The total number of rows.
                            count=len(TABLE_ROWS),
                            # The current setting within the `rowsPerPageOptions`.
                            rowsPerPage=5,
                            # The current page.
                            page=0,
                        ),
                    ],
                )
            ],
        )

    def _make_table_head(self) -> md.TableHead:
        return md.TableHead(
            children=[
                # The head of the table can contain several rows, e.g. to group columns into categories.
                md.TableRow(
                    children=[
                        md.TableCell(align="center", children=""),
                        md.TableCell(
                            align="center",
                            # The "information" category will spread on all columns but the first.
                            colSpan=len(TABLE_COLUMNS) - 1,
                            children="Information",
                        ),
                    ]
                ),
                md.TableRow(
                    children=[
                        md.TableCell(
                            align="right" if i > 0 else "left",
                            # Instead of raw text, `TableSortLabel` can be used to display a sorting control for each
                            # column.
                            children=md.TableSortLabel(
                                id=f"table-sort-{i}",
                                children=name,
                            ),
                        )
                        for i, name in enumerate(TABLE_COLUMNS)
                    ]
                ),
            ]
        )

    def register_callbacks(self, app: Dash, feedback_output: Output):
        num_columns = len(TABLE_COLUMNS)

        # Updates the body of the table based on pagination and sorting controls.
        @app.callback(
            Output("table-body", "children"),
            [
                Input("table-pagination", "page"),
                Input("table-pagination", "rowsPerPage"),
            ]
            + [
                Input(f"table-sort-{i}", prop)
                for i in range(num_columns)
                for prop in ["active", "direction"]
            ],
        )
        def on_pagination_change(
            page: int, rows_per_page: int, *sort_inputs: Union[bool, str]
        ):
            # `sort_inputs` contains the "active" and "direction" properties for each `TableSortLabel` component.
            sort_actives: Tuple[bool] = sort_inputs[::2]
            sort_directions: Tuple[str] = sort_inputs[1::2]
            # Finds the first active sort label in the list, otherwise defaults to the first column.
            current_sort_idx = (
                next((i for i, x in enumerate(sort_actives) if x), None) or 0
            )
            current_sort_direction = sort_directions[current_sort_idx] or "asc"

            ordered_rows = sorted(
                TABLE_ROWS,
                key=lambda r: r[current_sort_idx],
                reverse=current_sort_direction == "desc",
            )
            # Selects the current page using the state of the `TablePagination` component.
            rows = ordered_rows[
                page * rows_per_page : min((page + 1) * rows_per_page, len(TABLE_ROWS))
            ]
            return [
                md.TableRow(
                    sx={"&:last-child td, &:last-child th": {"border": 0}},
                    children=[
                        md.TableCell(
                            component="th" if i == 0 else None,
                            scope="row" if i == 0 else None,
                            align="right" if i > 0 else "left",
                            children=value,
                        )
                        for i, value in enumerate(row)
                    ],
                )
                for row in rows
            ]

        # Updates the states of the sorting controls.
        @app.callback(
            [
                Output(f"table-sort-{i}", prop)
                for i in range(num_columns)
                for prop in ["active", "direction"]
            ],
            [Input(f"table-sort-{i}", "n_clicks") for i in range(num_columns)],
            [
                State(f"table-sort-{i}", prop)
                for i in range(num_columns)
                for prop in ["active", "direction"]
            ],
        )
        def on_sort_change(*args: Union[bool, str]):
            states = args[num_columns:]
            already_active: Tuple[bool] = states[::2]
            current_direction: Tuple[str] = states[1::2]

            outputs = [False, "asc"] * num_columns

            ctx = dash.callback_context
            if ctx.triggered:
                sort_id = ctx.triggered[0]["prop_id"].split(".")[0]
                sort_idx = int(sort_id.split("-")[-1])
                # Setting the clicked sort label as the active one.
                outputs[sort_idx * 2] = True
                # Reverting the sort order if the clicked label was already active.
                outputs[sort_idx * 2 + 1] = (
                    "desc"
                    if already_active[sort_idx] and current_direction[sort_idx] == "asc"
                    else "asc"
                )

            return outputs
