# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ButtonUnstyled(Component):
    """A ButtonUnstyled component.
Material-UI ButtonUnstyled.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- key (string | number; optional)

- ref (boolean | number | string | dict | list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ButtonUnstyled'
    @_explicitize_args
    def __init__(self, ref=Component.UNDEFINED, key=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'ref']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'ref']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ButtonUnstyled, self).__init__(**args)
