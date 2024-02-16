# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Collapse(Component):
    """A Collapse component.
Material-UI Collapse.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content node to be collapsed.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- appear (boolean; optional):
    Normally a component is not transitioned if it is shown when the
    `<Transition>` component mounts. If you want to transition on the
    first mount set  appear to True, and the component will transition
    in as soon as the `<Transition>` mounts. Note: there are no
    specific \"appear\" states. appear only adds an additional enter
    transition.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- collapsedSize (string | number; optional):
    The width (horizontal) or height (vertical) of the container when
    collapsed.

- component (boolean | number | string | dict | list | a value equal to: "object", "style", "div", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noindex", "noscript", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "slot", "script", "section", "select", "small", "source", "span", "strong", "sub", "summary", "sup", "table", "template", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr", "webview"; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

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

- orientation (a value equal to: "horizontal", "vertical"; optional):
    The transition orientation.

- ref (boolean | number | string | dict | list; optional)

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- timeout (number | boolean | number | string | dict | list | a value equal to: "auto"; optional):
    The duration for the transition, in milliseconds. You may specify
    a single timeout for all transitions, or individually with an
    object.  Set to 'auto' to automatically calculate transition time
    based on height.

- unmountOnExit (boolean; optional):
    By default the child component stays mounted after it reaches the
    'exited' state. Set `unmountOnExit` if you'd prefer to unmount the
    component after it finishes exiting."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Collapse'
    @_explicitize_args
    def __init__(self, children=None, className=Component.UNDEFINED, classes=Component.UNDEFINED, collapsedSize=Component.UNDEFINED, component=Component.UNDEFINED, easing=Component.UNDEFINED, orientation=Component.UNDEFINED, timeout=Component.UNDEFINED, sx=Component.UNDEFINED, style=Component.UNDEFINED, mountOnEnter=Component.UNDEFINED, unmountOnExit=Component.UNDEFINED, enter=Component.UNDEFINED, appear=Component.UNDEFINED, exit=Component.UNDEFINED, ref=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'appear', 'className', 'classes', 'collapsedSize', 'component', 'easing', 'enter', 'exit', 'in', 'mountOnEnter', 'orientation', 'ref', 'style', 'sx', 'timeout', 'unmountOnExit']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'appear', 'className', 'classes', 'collapsedSize', 'component', 'easing', 'enter', 'exit', 'in', 'mountOnEnter', 'orientation', 'ref', 'style', 'sx', 'timeout', 'unmountOnExit']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Collapse, self).__init__(children=children, **args)
