# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ImageList(Component):
    """An ImageList component.
Material-UI ImageList.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component, normally `ImageListItem`s.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- cols (number; optional):
    Number of columns.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- gap (number; optional):
    The gap between items in px.

- rowHeight (number | a value equal to: "auto"; optional):
    The height of one row in px.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "standard", "masonry", "quilted", "woven"; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ImageList'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, cols=Component.UNDEFINED, gap=Component.UNDEFINED, rowHeight=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'cols', 'component', 'gap', 'rowHeight', 'style', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'cols', 'component', 'gap', 'rowHeight', 'style', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ImageList, self).__init__(children=children, **args)
