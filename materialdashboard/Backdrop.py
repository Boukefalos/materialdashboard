# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Backdrop(Component):
    """A Backdrop component.
Material-UI Backdrop.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- appear (boolean; optional):
    Perform the enter transition when it first mounts if `in` is also
    `True`. Set this to `False` to disable this behavior.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the Backdrop. Either a
    string to use a HTML element or a component.

- componentsProps (boolean | number | string | dict | list; optional):
    The props used for each slot inside the Backdrop.

- easing (string | boolean | number | string | dict | list; optional):
    The transition timing function. You may specify a single easing or
    a object containing enter and exit values.

- enter (boolean; optional):
    Enable or disable enter transitions.

- exit (boolean; optional):
    Enable or disable exit transitions.

- in (boolean; optional):
    If `True`, the component will transition in.

- invisible (boolean; optional):
    If `True`, the backdrop is invisible. It can be used when
    rendering a popover or a custom select component.

- mountOnEnter (boolean; optional):
    By default the child component is mounted immediately along with
    the parent Transition component. If you want to \"lazy mount\" the
    component on the first `in={True}` you can set `mountOnEnter`.
    After the first enter transition the component will stay mounted,
    even on \"exited\", unless you also specify `unmountOnExit`.

- open (boolean; optional):
    If `True`, the component is shown.

- ref (boolean | number | string | dict | list; optional)

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- timeout (number | boolean | number | string | dict | list; optional):
    The duration for the transition, in milliseconds. You may specify
    a single timeout for all transitions, or individually with an
    object.

- transitionDuration (number | boolean | number | string | dict | list; optional):
    The duration for the transition, in milliseconds. You may specify
    a single timeout for all transitions, or individually with an
    object.

- unmountOnExit (boolean; optional):
    By default the child component stays mounted after it reaches the
    'exited' state. Set `unmountOnExit` if you'd prefer to unmount the
    component after it finishes exiting."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Backdrop'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, style=Component.UNDEFINED, ref=Component.UNDEFINED, mountOnEnter=Component.UNDEFINED, unmountOnExit=Component.UNDEFINED, timeout=Component.UNDEFINED, easing=Component.UNDEFINED, enter=Component.UNDEFINED, appear=Component.UNDEFINED, exit=Component.UNDEFINED, classes=Component.UNDEFINED, open=Component.UNDEFINED, sx=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, invisible=Component.UNDEFINED, className=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'appear', 'className', 'classes', 'component', 'components', 'componentsProps', 'easing', 'enter', 'exit', 'in', 'invisible', 'mountOnEnter', 'open', 'ref', 'style', 'sx', 'timeout', 'transitionDuration', 'unmountOnExit']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'appear', 'className', 'classes', 'component', 'components', 'componentsProps', 'easing', 'enter', 'exit', 'in', 'invisible', 'mountOnEnter', 'open', 'ref', 'style', 'sx', 'timeout', 'transitionDuration', 'unmountOnExit']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Backdrop, self).__init__(children=children, **args)
