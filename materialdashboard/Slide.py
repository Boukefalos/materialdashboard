# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Slide(Component):
    """A Slide component.
Material-UI Slide.

Keyword arguments:

- children (boolean | number | string | dict | list; optional):
    A single child content element.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- appear (boolean; optional):
    Perform the enter transition when it first mounts if `in` is also
    `True`. Set this to `False` to disable this behavior.

- container (string; optional):
    An HTML element, or a function that returns one. It's used to set
    the container the Slide is transitioning from. If specified, the
    ID of an existing element should be provided.

- direction (a value equal to: "left", "right", "up", "down"; optional):
    Direction the child node will enter from.

- easing (string | boolean | number | string | dict | list; optional):
    The transition timing function. You may specify a single easing or
    a object containing enter and exit values.

- enter (boolean; optional):
    Enable or disable enter transitions.

- exit (boolean; optional):
    Enable or disable exit transitions.

- in (boolean; optional):
    If `True`, the component will transition in.

- mountOnEnter (boolean; optional):
    By default the child component is mounted immediately along with
    the parent Transition component. If you want to \"lazy mount\" the
    component on the first `in={True}` you can set `mountOnEnter`.
    After the first enter transition the component will stay mounted,
    even on \"exited\", unless you also specify `unmountOnExit`.

- ref (boolean | number | string | dict | list; optional)

- style (boolean | number | string | dict | list; optional)

- timeout (number | boolean | number | string | dict | list; optional):
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
    _type = 'Slide'
    @_explicitize_args
    def __init__(self, children=None, appear=Component.UNDEFINED, container=Component.UNDEFINED, direction=Component.UNDEFINED, easing=Component.UNDEFINED, ref=Component.UNDEFINED, timeout=Component.UNDEFINED, style=Component.UNDEFINED, enter=Component.UNDEFINED, exit=Component.UNDEFINED, mountOnEnter=Component.UNDEFINED, unmountOnExit=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'appear', 'container', 'direction', 'easing', 'enter', 'exit', 'in', 'mountOnEnter', 'ref', 'style', 'timeout', 'unmountOnExit']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'appear', 'container', 'direction', 'easing', 'enter', 'exit', 'in', 'mountOnEnter', 'ref', 'style', 'timeout', 'unmountOnExit']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Slide, self).__init__(children=children, **args)
