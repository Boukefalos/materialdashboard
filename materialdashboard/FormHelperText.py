# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FormHelperText(Component):
    """A FormHelperText component.
Material-UI FormHelperText.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.  If `' '` is provided, the component
    reserves one line height for displaying a future message.

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

- disabled (boolean; optional):
    If `True`, the helper text should be displayed in a disabled
    state.

- error (boolean; optional):
    If `True`, helper text should be displayed in an error state.

- filled (boolean; optional):
    If `True`, the helper text should use filled classes key.

- focused (boolean; optional):
    If `True`, the helper text should use focused classes key.

- margin (string; optional):
    If `dense`, will adjust vertical spacing. This is normally
    obtained via context from FormControl.

- required (boolean; optional):
    If `True`, the helper text should use required classes key.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "outlined", "standard", "filled"; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'FormHelperText'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, filled=Component.UNDEFINED, focused=Component.UNDEFINED, margin=Component.UNDEFINED, required=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'component', 'disabled', 'error', 'filled', 'focused', 'margin', 'required', 'style', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'component', 'disabled', 'error', 'filled', 'focused', 'margin', 'required', 'style', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FormHelperText, self).__init__(children=children, **args)
