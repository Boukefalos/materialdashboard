# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SvgIcon(Component):
    """A SvgIcon component.
Material-UI SvgIcon.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Node passed into the SVG element.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- color (a value equal to: "inherit", "disabled", "action", "success", "info", "warning", "error", "primary", "secondary"; optional):
    The color of the component. It supports those theme colors that
    make sense for this component. You can use the `htmlColor` prop to
    apply a color attribute to the SVG element.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- fontSize (a value equal to: "small", "inherit", "medium", "large"; optional):
    The fontSize applied to the icon. Defaults to 24px, but can be
    configure to inherit font size.

- htmlColor (string; optional):
    Applies a color attribute to the SVG element.

- shapeRendering (string; optional):
    The shape-rendering attribute. The behavior of the different
    options is described on the [MDN Web
    Docs](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/shape-rendering).
    If you are having issues with blurry icons you should investigate
    this prop.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- titleAccess (string; optional):
    Provides a human-readable title for the element that contains it.
    https://www.w3.org/TR/SVG-access/#Equivalent.

- viewBox (string; optional):
    Allows you to redefine what the coordinates without units mean
    inside an SVG element. For example, if the SVG element is 500
    (width) by 200 (height), and you pass viewBox=\"0 0 50 20\", this
    means that the coordinates inside the SVG will go from the top
    left corner (0,0) to bottom right (50,20) and each unit will be
    worth 10px."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'SvgIcon'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, fontSize=Component.UNDEFINED, htmlColor=Component.UNDEFINED, shapeRendering=Component.UNDEFINED, sx=Component.UNDEFINED, titleAccess=Component.UNDEFINED, viewBox=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'color', 'component', 'fontSize', 'htmlColor', 'shapeRendering', 'style', 'sx', 'titleAccess', 'viewBox']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'color', 'component', 'fontSize', 'htmlColor', 'shapeRendering', 'style', 'sx', 'titleAccess', 'viewBox']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SvgIcon, self).__init__(children=children, **args)
