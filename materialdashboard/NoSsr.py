# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class NoSsr(Component):
    """A NoSsr component.
Material-UI NoSsr.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    You can wrap a node.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- defer (boolean; optional):
    If `True`, the component will not only prevent server-side
    rendering. It will also defer the rendering of the children into a
    different screen frame.

- fallback (boolean | number | string | dict | list; optional):
    The fallback content to display."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'NoSsr'
    @_explicitize_args
    def __init__(self, children=None, defer=Component.UNDEFINED, fallback=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'defer', 'fallback']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'defer', 'fallback']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(NoSsr, self).__init__(children=children, **args)
