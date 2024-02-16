# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ListSubheader(Component):
    """A ListSubheader component.
Material-UI ListSubheader.

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

- color (a value equal to: "inherit", "primary", "default"; optional):
    The color of the component. It supports those theme colors that
    make sense for this component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- disableGutters (boolean; optional):
    If `True`, the List Subheader will not have gutters.

- disableSticky (boolean; optional):
    If `True`, the List Subheader will not stick to the top during
    scroll.

- inset (boolean; optional):
    If `True`, the List Subheader is indented.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ListSubheader'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disableGutters=Component.UNDEFINED, disableSticky=Component.UNDEFINED, inset=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'color', 'component', 'disableGutters', 'disableSticky', 'inset', 'style', 'sx']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'color', 'component', 'disableGutters', 'disableSticky', 'inset', 'style', 'sx']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ListSubheader, self).__init__(children=children, **args)
