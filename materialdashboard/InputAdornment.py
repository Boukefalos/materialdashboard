# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class InputAdornment(Component):
    """An InputAdornment component.
Material-UI InputAdornment.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component, normally an `IconButton` or string.

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

- disablePointerEvents (boolean; optional):
    Disable pointer events on the root. This allows for the content of
    the adornment to focus the `input` on click.

- disableTypography (boolean; optional):
    If children is a string then disable wrapping in a Typography
    component.

- position (a value equal to: "end", "start"; optional):
    The position this adornment should appear relative to the `Input`.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "outlined", "standard", "filled"; optional):
    The variant to use. Note: If you are using the `TextField`
    component or the `FormControl` component you do not have to set
    this manually."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'InputAdornment'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, disablePointerEvents=Component.UNDEFINED, disableTypography=Component.UNDEFINED, position=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'component', 'disablePointerEvents', 'disableTypography', 'position', 'style', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'component', 'disablePointerEvents', 'disableTypography', 'position', 'style', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(InputAdornment, self).__init__(children=children, **args)
