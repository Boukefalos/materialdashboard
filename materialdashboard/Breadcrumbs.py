# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Breadcrumbs(Component):
    """A Breadcrumbs component.
Material-UI Breadcrumbs.

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

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- expandText (string; optional):
    Override the default label for the expand button.  For
    localization purposes, you can use the provided
    [translations](/guides/localization/).

- itemsAfterCollapse (number; optional):
    If max items is exceeded, the number of items to show after the
    ellipsis.

- itemsBeforeCollapse (number; optional):
    If max items is exceeded, the number of items to show before the
    ellipsis.

- maxItems (number; optional):
    Specifies the maximum number of breadcrumbs to display. When there
    are more than the maximum number, only the first
    `itemsBeforeCollapse` and last `itemsAfterCollapse` will be shown,
    with an ellipsis in between.

- separator (boolean | number | string | dict | list; optional):
    Custom separator node.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Breadcrumbs'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, classes=Component.UNDEFINED, expandText=Component.UNDEFINED, itemsAfterCollapse=Component.UNDEFINED, itemsBeforeCollapse=Component.UNDEFINED, maxItems=Component.UNDEFINED, separator=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'component', 'expandText', 'itemsAfterCollapse', 'itemsBeforeCollapse', 'maxItems', 'separator', 'style', 'sx']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'component', 'expandText', 'itemsAfterCollapse', 'itemsBeforeCollapse', 'maxItems', 'separator', 'style', 'sx']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Breadcrumbs, self).__init__(children=children, **args)
