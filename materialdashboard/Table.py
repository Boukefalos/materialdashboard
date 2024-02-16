# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Table(Component):
    """A Table component.
Material-UI Table.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the table, normally `TableHead` and `TableBody`.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- padding (a value equal to: "checkbox", "none", "normal"; optional):
    Allows TableCells to inherit padding of the Table.

- size (a value equal to: "small", "medium"; optional):
    Allows TableCells to inherit size of the Table.

- stickyHeader (boolean; optional):
    Set the header sticky.  ⚠️ It doesn't work with IE11.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Table'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, padding=Component.UNDEFINED, size=Component.UNDEFINED, stickyHeader=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'component', 'padding', 'size', 'stickyHeader', 'style', 'sx']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'component', 'padding', 'size', 'stickyHeader', 'style', 'sx']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Table, self).__init__(children=children, **args)
