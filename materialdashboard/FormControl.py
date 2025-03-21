# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FormControl(Component):
    """A FormControl component.
Material-UI FormControl.

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

- color (a value equal to: "success", "info", "warning", "error", "primary", "secondary"; optional):
    The color of the component. It supports those theme colors that
    make sense for this component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- disabled (boolean; optional):
    If `True`, the label, input and helper text should be displayed in
    a disabled state.

- error (boolean; optional):
    If `True`, the label is displayed in an error state.

- focused (boolean; optional):
    If `True`, the component is displayed in focused state.

- fullWidth (boolean; optional):
    If `True`, the component will take up the full width of its
    container.

- hiddenLabel (boolean; optional):
    If `True`, the label is hidden. This is used to increase density
    for a `FilledInput`. Be sure to add `aria-label` to the `input`
    element.

- margin (a value equal to: "none", "normal", "dense"; optional):
    If `dense` or `normal`, will adjust vertical spacing of this and
    contained components.

- required (boolean; optional):
    If `True`, the label will indicate that the `input` is required.

- size (a value equal to: "small", "medium"; optional):
    The size of the component.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "outlined", "standard", "filled"; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'FormControl'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, error=Component.UNDEFINED, fullWidth=Component.UNDEFINED, focused=Component.UNDEFINED, hiddenLabel=Component.UNDEFINED, margin=Component.UNDEFINED, required=Component.UNDEFINED, size=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'color', 'component', 'disabled', 'error', 'focused', 'fullWidth', 'hiddenLabel', 'margin', 'required', 'size', 'style', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'color', 'component', 'disabled', 'error', 'focused', 'fullWidth', 'hiddenLabel', 'margin', 'required', 'size', 'style', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FormControl, self).__init__(children=children, **args)
