# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Chip(Component):
    """A Chip component.
Material-UI Chip.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- avatar (dict; optional):
    The Avatar element to display.

    `avatar` is a dict with keys:

    - children (string; optional)

    - src (string; optional)

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- clickable (boolean; optional):
    If `True`, the chip will appear clickable, and will raise when
    pressed, even if the onClick prop is not defined. If `False`, the
    chip will not appear clickable, even if onClick prop is defined.
    This can be used, for example, along with the component prop to
    indicate an anchor Chip is clickable. Note: this controls the UI
    and does not affect the onClick event.

- color (a value equal to: "success", "info", "warning", "error", "primary", "secondary", "default"; optional):
    The color of the component. It supports those theme colors that
    make sense for this component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- deleteIcon (boolean | string; default False):
    Override the default delete icon element. Shown only if `onDelete`
    is set.

- disabled (boolean; optional):
    If `True`, the component is disabled.

- icon (string; optional):
    Icon element.

- label (boolean | number | string | dict | list; optional):
    The content of the component.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- n_deletes (number; default 0):
    An integer that represents the number of times that the delete
    icon has been clicked on.

- size (a value equal to: "small", "medium"; optional):
    The size of the component.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- variant (a value equal to: "outlined", "filled"; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Chip'
    @_explicitize_args
    def __init__(self, component=Component.UNDEFINED, avatar=Component.UNDEFINED, classes=Component.UNDEFINED, clickable=Component.UNDEFINED, color=Component.UNDEFINED, deleteIcon=Component.UNDEFINED, disabled=Component.UNDEFINED, icon=Component.UNDEFINED, label=Component.UNDEFINED, size=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_deletes=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'avatar', 'className', 'classes', 'clickable', 'color', 'component', 'deleteIcon', 'disabled', 'icon', 'label', 'n_clicks', 'n_deletes', 'size', 'style', 'sx', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'avatar', 'className', 'classes', 'clickable', 'color', 'component', 'deleteIcon', 'disabled', 'icon', 'label', 'n_clicks', 'n_deletes', 'size', 'style', 'sx', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Chip, self).__init__(**args)
