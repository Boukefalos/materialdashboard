# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ClickAwayListener(Component):
    """A ClickAwayListener component.
Material-UI ClickAwayListener.

Keyword arguments:

- children (boolean | number | string | dict | list; optional):
    The wrapped element.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- disableReactTree (boolean; optional):
    If `True`, the React tree is ignored and only the DOM tree is
    considered.  This prop changes how portaled elements are handled.

- mouseEvent (a value equal to: false, "onClick", "onMouseDown", "onMouseUp"; optional):
    The mouse event to listen to. You can disable the listener by
    providing `False`.

- touchEvent (a value equal to: false, "onTouchEnd", "onTouchStart"; optional):
    The touch event to listen to. You can disable the listener by
    providing `False`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ClickAwayListener'
    @_explicitize_args
    def __init__(self, children=None, disableReactTree=Component.UNDEFINED, mouseEvent=Component.UNDEFINED, touchEvent=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'disableReactTree', 'mouseEvent', 'touchEvent']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'disableReactTree', 'mouseEvent', 'touchEvent']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ClickAwayListener, self).__init__(children=children, **args)
