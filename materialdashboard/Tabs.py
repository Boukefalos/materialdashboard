# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tabs(Component):
    """A Tabs component.
Material-UI Tabs.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- ScrollButtonComponent (boolean | number | string | dict | list | a value equal to: "symbol", "object", "style", "div", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noindex", "noscript", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "slot", "script", "section", "select", "small", "source", "span", "strong", "sub", "summary", "sup", "table", "template", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr", "webview", "svg", "animate", "animateMotion", "animateTransform", "circle", "clipPath", "defs", "desc", "ellipse", "feBlend", "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow", "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur", "feImage", "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight", "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence", "filter", "foreignObject", "g", "image", "line", "linearGradient", "marker", "mask", "metadata", "mpath", "path", "pattern", "polygon", "polyline", "radialGradient", "rect", "stop", "switch", "text", "textPath", "tspan", "use", "view"; optional):
    The component used to render the scroll buttons.

- TabIndicatorProps (boolean | number | string | dict | list; optional):
    Props applied to the tab indicator element.

- TabScrollButtonProps (boolean | number | string | dict | list; optional):
    Props applied to the [`TabScrollButton`](/api/tab-scroll-button/)
    element.

- action (boolean | number | string | dict | list; optional):
    Callback fired when the component mounts. This is useful when you
    want to trigger an action programmatically. It supports two
    actions: `updateIndicator()` and `updateScrollButtons()`.

- allowScrollButtonsMobile (boolean; optional):
    If `True`, the scroll buttons aren't forced hidden on mobile. By
    default the scroll buttons are hidden on mobile and takes
    precedence over `scrollButtons`.

- centered (boolean; optional):
    If `True`, the tabs are centered. This prop is intended for large
    views.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- indicatorColor (a value equal to: "primary", "secondary"; optional):
    Determines the color of the indicator.

- orientation (a value equal to: "horizontal", "vertical"; optional):
    The component orientation (layout flow direction).

- scrollButtons (a value equal to: false, true, "auto"; optional):
    Determine behavior of scroll buttons when tabs are set to scroll:
    - `auto` will only present them when not all the items are
    visible. - `True` will always present them. - `False` will never
    present them.  By default the scroll buttons are hidden on mobile.
    This behavior can be disabled with `allowScrollButtonsMobile`.

- selectionFollowsFocus (boolean; optional):
    If `True` the selected tab changes on focus. Otherwise it only
    changes on activation.

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- textColor (a value equal to: "inherit", "primary", "secondary"; optional):
    Determines the color of the `Tab`.

- value (boolean | number | string | dict | list; optional):
    The value of the currently selected `Tab`. If you don't want any
    selected `Tab`, you can set this prop to `False`.

- variant (a value equal to: "standard", "fullWidth", "scrollable"; optional):
    Determines additional display behavior of the tabs:  -
    `scrollable` will invoke scrolling properties and allow for
    horizontally scrolling (or swiping) of the tab bar. -`fullWidth`
    will make the tabs grow to use all the available space, which
    should be used for small views, like on mobile. - `standard` will
    render the default state.

- visibleScrollbar (boolean; optional):
    If `True`, the scrollbar is visible. It can be useful when
    displaying a long vertical list of tabs."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Tabs'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, action=Component.UNDEFINED, allowScrollButtonsMobile=Component.UNDEFINED, centered=Component.UNDEFINED, classes=Component.UNDEFINED, indicatorColor=Component.UNDEFINED, orientation=Component.UNDEFINED, ScrollButtonComponent=Component.UNDEFINED, scrollButtons=Component.UNDEFINED, selectionFollowsFocus=Component.UNDEFINED, TabIndicatorProps=Component.UNDEFINED, TabScrollButtonProps=Component.UNDEFINED, textColor=Component.UNDEFINED, value=Component.UNDEFINED, variant=Component.UNDEFINED, visibleScrollbar=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'ScrollButtonComponent', 'TabIndicatorProps', 'TabScrollButtonProps', 'action', 'allowScrollButtonsMobile', 'centered', 'className', 'classes', 'component', 'indicatorColor', 'orientation', 'scrollButtons', 'selectionFollowsFocus', 'style', 'sx', 'textColor', 'value', 'variant', 'visibleScrollbar']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ScrollButtonComponent', 'TabIndicatorProps', 'TabScrollButtonProps', 'action', 'allowScrollButtonsMobile', 'centered', 'className', 'classes', 'component', 'indicatorColor', 'orientation', 'scrollButtons', 'selectionFollowsFocus', 'style', 'sx', 'textColor', 'value', 'variant', 'visibleScrollbar']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tabs, self).__init__(children=children, **args)
