# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ButtonGroup(Component):
    """A ButtonGroup component.
Material-UI ButtonGroup.

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

- color (a value equal to: "inherit", "success", "info", "warning", "error", "primary", "secondary"; optional):
    The color of the component. It supports those theme colors that
    make sense for this component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- disableElevation (boolean; optional):
    If `True`, no elevation is used.

- disableFocusRipple (boolean; optional):
    If `True`, the button keyboard focus ripple is disabled.

- disableRipple (boolean; optional):
    If `True`, the button ripple effect is disabled.

- disabled (boolean; optional):
    If `True`, the component is disabled.

- fullWidth (boolean; optional):
    If `True`, the buttons will take up the full width of its
    container.

- orientation (a value equal to: "horizontal", "vertical"; optional):
    The component orientation (layout flow direction).

- size (a value equal to: "small", "medium", "large"; optional):
    The size of the component. `small` is equivalent to the dense
    button styling.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "text", "outlined", "contained"; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ButtonGroup'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, disableElevation=Component.UNDEFINED, disableFocusRipple=Component.UNDEFINED, disableRipple=Component.UNDEFINED, fullWidth=Component.UNDEFINED, orientation=Component.UNDEFINED, size=Component.UNDEFINED, variant=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'color', 'component', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'fullWidth', 'orientation', 'size', 'style', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'color', 'component', 'disableElevation', 'disableFocusRipple', 'disableRipple', 'disabled', 'fullWidth', 'orientation', 'size', 'style', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ButtonGroup, self).__init__(children=children, **args)
