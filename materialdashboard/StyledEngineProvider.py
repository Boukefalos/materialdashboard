# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class StyledEngineProvider(Component):
    """A StyledEngineProvider component.
Material-UI StyledEngineProvider.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- injectFirst (boolean; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'StyledEngineProvider'
    @_explicitize_args
    def __init__(self, children=None, injectFirst=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'injectFirst']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'injectFirst']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(StyledEngineProvider, self).__init__(children=children, **args)
