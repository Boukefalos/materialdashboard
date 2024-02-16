# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Unstable_TrapFocus(Component):
    """An Unstable_TrapFocus component.
Material-UI Unstable_TrapFocus.

Keyword arguments:

- children (boolean | number | string | dict | list; optional):
    A single child content element.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- disableAutoFocus (boolean; optional):
    If `True`, the trap focus will not automatically shift focus to
    itself when it opens, and replace it to the last focused element
    when it closes. This also works correctly with any trap focus
    children that have the `disableAutoFocus` prop.  Generally this
    should never be set to `True` as it makes the trap focus less
    accessible to assistive technologies, like screen readers.

- disableEnforceFocus (boolean; optional):
    If `True`, the trap focus will not prevent focus from leaving the
    trap focus while open.  Generally this should never be set to
    `True` as it makes the trap focus less accessible to assistive
    technologies, like screen readers.

- disableRestoreFocus (boolean; optional):
    If `True`, the trap focus will not restore focus to previously
    focused element once trap focus is hidden.

- open (boolean; optional):
    If `True`, focus is locked."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Unstable_TrapFocus'
    @_explicitize_args
    def __init__(self, children=None, open=Component.UNDEFINED, disableAutoFocus=Component.UNDEFINED, disableEnforceFocus=Component.UNDEFINED, disableRestoreFocus=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'disableAutoFocus', 'disableEnforceFocus', 'disableRestoreFocus', 'open']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'disableAutoFocus', 'disableEnforceFocus', 'disableRestoreFocus', 'open']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Unstable_TrapFocus, self).__init__(children=children, **args)
