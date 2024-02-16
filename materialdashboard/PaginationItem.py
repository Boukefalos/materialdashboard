# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PaginationItem(Component):
    """A PaginationItem component.
Material-UI PaginationItem.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- color (a value equal to: "standard", "primary", "secondary"; optional):
    The active color.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- disabled (boolean; optional):
    If `True`, the component is disabled.

- page (boolean | number | string | dict | list; optional):
    The current page number.

- selected (boolean; optional):
    If `True` the pagination item is selected.

- shape (a value equal to: "rounded", "circular"; optional):
    The shape of the pagination item.

- size (a value equal to: "small", "medium", "large"; optional):
    The size of the component.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- type (a value equal to: "page", "next", "previous", "first", "last", "start-ellipsis", "end-ellipsis"; optional):
    The type of pagination item.

- variant (a value equal to: "text", "outlined"; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'PaginationItem'
    @_explicitize_args
    def __init__(self, component=Component.UNDEFINED, classes=Component.UNDEFINED, color=Component.UNDEFINED, disabled=Component.UNDEFINED, page=Component.UNDEFINED, selected=Component.UNDEFINED, shape=Component.UNDEFINED, size=Component.UNDEFINED, sx=Component.UNDEFINED, type=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'classes', 'color', 'component', 'disabled', 'page', 'selected', 'shape', 'size', 'style', 'sx', 'type', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'classes', 'color', 'component', 'disabled', 'page', 'selected', 'shape', 'size', 'style', 'sx', 'type', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(PaginationItem, self).__init__(**args)
