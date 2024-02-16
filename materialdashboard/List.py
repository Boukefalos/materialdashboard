# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class List(Component):
    """A List component.
Material-UI List.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

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

- dense (boolean; optional):
    If `True`, compact vertical padding designed for keyboard and
    mouse input is used for the list and list items. The prop is
    available to descendant components as the `dense` context.

- disablePadding (boolean; optional):
    If `True`, vertical padding is removed from the list.

- style (boolean | number | string | dict | list; optional)

- subheader (boolean | number | string | dict | list; optional):
    The content of the subheader, normally `ListSubheader`.

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'List'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, dense=Component.UNDEFINED, disablePadding=Component.UNDEFINED, subheader=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'component', 'dense', 'disablePadding', 'style', 'subheader', 'sx']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'component', 'dense', 'disablePadding', 'style', 'subheader', 'sx']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(List, self).__init__(children=children, **args)
