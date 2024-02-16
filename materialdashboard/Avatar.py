# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Avatar(Component):
    """An Avatar component.
Material-UI Avatar.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Used to render icon or text elements inside the Avatar if `src` is
    not set. This can be an element, or just a string.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- alt (string; optional):
    Used in combination with `src` or `srcSet` to provide an alt
    attribute for the rendered `img` element.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- imgProps (boolean | number | string | dict | list; optional):
    [Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attributes)
    applied to the `img` element if the component is used to display
    an image. It can be used to listen for the loading error event.

- sizes (string; optional):
    The `sizes` attribute for the `img` element.

- src (string; optional):
    The `src` attribute for the `img` element.

- srcSet (string; optional):
    The `srcSet` attribute for the `img` element. Use this attribute
    for responsive image display.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "square", "rounded", "circular"; optional):
    The shape of the avatar."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Avatar'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, alt=Component.UNDEFINED, classes=Component.UNDEFINED, imgProps=Component.UNDEFINED, sizes=Component.UNDEFINED, src=Component.UNDEFINED, srcSet=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'alt', 'className', 'classes', 'component', 'imgProps', 'sizes', 'src', 'srcSet', 'style', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alt', 'className', 'classes', 'component', 'imgProps', 'sizes', 'src', 'srcSet', 'style', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Avatar, self).__init__(children=children, **args)
