# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GlobalStyles(Component):
    """A GlobalStyles component.
Material-UI GlobalStyles.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- styles (string | number | boolean | number | string | dict | list | a value equal to: false, true; optional):
    The styles you want to apply globally."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'GlobalStyles'
    @_explicitize_args
    def __init__(self, styles=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'styles']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'styles']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(GlobalStyles, self).__init__(**args)
