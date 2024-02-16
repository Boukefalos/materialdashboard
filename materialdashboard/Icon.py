# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Icon(Component):
    """An Icon component.
Material-UI Icon.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The name of the icon font ligature.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- baseClassName (string; optional):
    The base class applied to the icon. Defaults to 'material-icons',
    but can be changed to any other base class that suits the icon
    font you're using (e.g. material-icons-rounded, fas, etc).

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- color (a value equal to: "inherit", "disabled", "action", "success", "info", "warning", "error", "primary", "secondary"; optional):
    The color of the component. It supports those theme colors that
    make sense for this component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- fontSize (a value equal to: "small", "inherit", "medium", "large"; optional):
    The fontSize applied to the icon. Defaults to 24px, but can be
    configure to inherit font size.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Icon'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, baseClassName=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, fontSize=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'baseClassName', 'className', 'classes', 'color', 'component', 'fontSize', 'style', 'sx']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'baseClassName', 'className', 'classes', 'color', 'component', 'fontSize', 'style', 'sx']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Icon, self).__init__(children=children, **args)
