# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ExtendButton(Component):
    """An ExtendButton component.
Material-UI ExtendButton.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- LinkComponent (boolean | number | string | dict | list | a value equal to: "symbol", "object", "style", "div", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noindex", "noscript", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "slot", "script", "section", "select", "small", "source", "span", "strong", "sub", "summary", "sup", "table", "template", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr", "webview", "svg", "animate", "animateMotion", "animateTransform", "circle", "clipPath", "defs", "desc", "ellipse", "feBlend", "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow", "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur", "feImage", "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight", "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence", "filter", "foreignObject", "g", "image", "line", "linearGradient", "marker", "mask", "metadata", "mpath", "path", "pattern", "polygon", "polyline", "radialGradient", "rect", "stop", "switch", "text", "textPath", "tspan", "use", "view"; optional):
    The component used to render a link when the `href` prop is
    provided.

- TouchRippleProps (boolean | number | string | dict | list; optional):
    Props applied to the `TouchRipple` element.

- action (boolean | number | string | dict | list; optional):
    A ref for imperative actions. It currently only supports
    `focusVisible()` action.

- centerRipple (boolean; optional):
    If `True`, the ripples are centered. They won't start at the
    cursor interaction position.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- disableRipple (boolean; optional):
    If `True`, the ripple effect is disabled.  ⚠️ Without a ripple
    there is no styling for :focus-visible by default. Be sure to
    highlight the element by applying separate styles with the
    `.Mui-focusVisible` class.

- disableTouchRipple (boolean; optional):
    If `True`, the touch ripple effect is disabled.

- disabled (boolean; optional):
    If `True`, the component is disabled.

- focusRipple (boolean; optional):
    If `True`, the base button will have a keyboard focus ripple.

- focusVisibleClassName (string; optional):
    This prop can help identify which element has keyboard focus. The
    class name will be applied when the element gains the focus
    through keyboard interaction. It's a polyfill for the [CSS
    :focus-visible
    selector](https://drafts.csswg.org/selectors-4/#the-focus-visible-pseudo).
    The rationale for using this feature [is explained
    here](https://github.com/WICG/focus-visible/blob/master/explainer.md).
    A [polyfill can be used](https://github.com/WICG/focus-visible) to
    apply a `focus-visible` class to other components if needed.

- href (string; optional)

- style (boolean | number | string | dict | list; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- tabIndex (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ExtendButton'
    @_explicitize_args
    def __init__(self, children=None, href=Component.UNDEFINED, sx=Component.UNDEFINED, tabIndex=Component.UNDEFINED, disabled=Component.UNDEFINED, action=Component.UNDEFINED, centerRipple=Component.UNDEFINED, disableRipple=Component.UNDEFINED, disableTouchRipple=Component.UNDEFINED, focusRipple=Component.UNDEFINED, focusVisibleClassName=Component.UNDEFINED, LinkComponent=Component.UNDEFINED, TouchRippleProps=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, classes=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'LinkComponent', 'TouchRippleProps', 'action', 'centerRipple', 'className', 'classes', 'disableRipple', 'disableTouchRipple', 'disabled', 'focusRipple', 'focusVisibleClassName', 'href', 'style', 'sx', 'tabIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'LinkComponent', 'TouchRippleProps', 'action', 'centerRipple', 'className', 'classes', 'disableRipple', 'disableTouchRipple', 'disabled', 'focusRipple', 'focusVisibleClassName', 'href', 'style', 'sx', 'tabIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ExtendButton, self).__init__(children=children, **args)
