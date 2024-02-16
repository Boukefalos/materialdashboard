# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SwitchUnstyled(Component):
    """A SwitchUnstyled component.
Material-UI SwitchUnstyled.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- checked (boolean; optional):
    If `True`, the component is checked.

- className (string; optional):
    Class name applied to the root element.

- component (boolean | number | string | dict | list | a value equal to: "symbol", "object", "style", "div", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noindex", "noscript", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "slot", "script", "section", "select", "small", "source", "span", "strong", "sub", "summary", "sup", "table", "template", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr", "webview", "svg", "animate", "animateMotion", "animateTransform", "circle", "clipPath", "defs", "desc", "ellipse", "feBlend", "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow", "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur", "feImage", "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight", "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence", "filter", "foreignObject", "g", "image", "line", "linearGradient", "marker", "mask", "metadata", "mpath", "path", "pattern", "polygon", "polyline", "radialGradient", "rect", "stop", "switch", "text", "textPath", "tspan", "use", "view"; optional):
    The component used for the Root slot.  Either a string to use a
    HTML element or a component.  This is equivalent to
    `components.Root`. If both are provided, the `component` is used.

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the Switch.  Either a
    string to use a HTML element or a component.

- componentsProps (boolean | number | string | dict | list; optional):
    The props used for each slot inside the Switch.

- defaultChecked (boolean; optional):
    The default checked state. Use when the component is not
    controlled.

- disabled (boolean; optional):
    If `True`, the component is disabled.

- key (string | number; optional)

- readOnly (boolean; optional):
    If `True`, the component is read only.

- ref (boolean | number | string | dict | list; optional)

- required (boolean; optional):
    If `True`, the `input` element is required."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'SwitchUnstyled'
    @_explicitize_args
    def __init__(self, className=Component.UNDEFINED, component=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, checked=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, disabled=Component.UNDEFINED, readOnly=Component.UNDEFINED, required=Component.UNDEFINED, ref=Component.UNDEFINED, key=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'checked', 'className', 'component', 'components', 'componentsProps', 'defaultChecked', 'disabled', 'key', 'readOnly', 'ref', 'required']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'checked', 'className', 'component', 'components', 'componentsProps', 'defaultChecked', 'disabled', 'key', 'readOnly', 'ref', 'required']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(SwitchUnstyled, self).__init__(**args)
