# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Skeleton(Component):
    """A Skeleton component.
Material-UI Skeleton.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Optional children to infer width and height from.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- animation (a value equal to: false, "pulse", "wave"; optional):
    The animation. If `False` the animation effect is disabled.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- height (string | number; optional):
    Height of the skeleton. Useful when you don't want to adapt the
    skeleton to a text element but for instance a card.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "text", "circular", "rectangular"; optional):
    The type of content that will be rendered.

- width (string | number; optional):
    Width of the skeleton. Useful when the skeleton is inside an
    inline element with no width of its own."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Skeleton'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, animation=Component.UNDEFINED, classes=Component.UNDEFINED, height=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, width=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'animation', 'className', 'classes', 'component', 'height', 'style', 'sx', 'variant', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'animation', 'className', 'classes', 'component', 'height', 'style', 'sx', 'variant', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Skeleton, self).__init__(children=children, **args)
