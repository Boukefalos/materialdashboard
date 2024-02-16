# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Divider(Component):
    """A Divider component.
Material-UI Divider.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- absolute (boolean; optional):
    Absolutely position the element.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- flexItem (boolean; optional):
    If `True`, a vertical divider will have the correct height when
    used in flex container. (By default, a vertical divider will have
    a calculated height of `0px` if it is the child of a flex
    container.).

- light (boolean; optional):
    If `True`, the divider will have a lighter color.

- orientation (a value equal to: "horizontal", "vertical"; optional):
    The component orientation.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- textAlign (a value equal to: "left", "right", "center"; optional):
    The text alignment.

- variant (a value equal to: "inset", "middle", "fullWidth"; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Divider'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, absolute=Component.UNDEFINED, classes=Component.UNDEFINED, flexItem=Component.UNDEFINED, light=Component.UNDEFINED, orientation=Component.UNDEFINED, sx=Component.UNDEFINED, textAlign=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'absolute', 'className', 'classes', 'component', 'flexItem', 'light', 'orientation', 'style', 'sx', 'textAlign', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'absolute', 'className', 'classes', 'component', 'flexItem', 'light', 'orientation', 'style', 'sx', 'textAlign', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Divider, self).__init__(children=children, **args)
