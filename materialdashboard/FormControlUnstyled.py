# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FormControlUnstyled(Component):
    """A FormControlUnstyled component.
Material-UI FormControlUnstyled.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- className (string; optional):
    Class name applied to the root element.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the FormControl.  Either
    a string to use a HTML element or a component.

- componentsProps (boolean | number | string | dict | list; optional)

- defaultValue (boolean | number | string | dict | list; optional)

- disabled (boolean; optional):
    If `True`, the label, input and helper text should be displayed in
    a disabled state.

- error (boolean; optional):
    If `True`, the label is displayed in an error state.

- extraContextProperties (boolean | number | string | dict | list; optional):
    Extra properties to be placed on the FormControlContext.

- focused (boolean; optional):
    If `True`, the component is displayed in focused state.

- required (boolean; optional):
    If `True`, the label will indicate that the `input` is required.

- value (boolean | number | string | dict | list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'FormControlUnstyled'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, className=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, extraContextProperties=Component.UNDEFINED, focused=Component.UNDEFINED, required=Component.UNDEFINED, value=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'component', 'components', 'componentsProps', 'defaultValue', 'disabled', 'error', 'extraContextProperties', 'focused', 'required', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'component', 'components', 'componentsProps', 'defaultValue', 'disabled', 'error', 'extraContextProperties', 'focused', 'required', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FormControlUnstyled, self).__init__(children=children, **args)
