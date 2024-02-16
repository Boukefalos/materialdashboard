# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MenuItem(Component):
    """A MenuItem component.
Material-UI MenuItem.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional)

- LinkComponent (boolean | number | string | dict | list | a value equal to: "symbol", "object", "style", "div", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noindex", "noscript", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "slot", "script", "section", "select", "small", "source", "span", "strong", "sub", "summary", "sup", "table", "template", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr", "webview", "svg", "animate", "animateMotion", "animateTransform", "circle", "clipPath", "defs", "desc", "ellipse", "feBlend", "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow", "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur", "feImage", "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight", "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence", "filter", "foreignObject", "g", "image", "line", "linearGradient", "marker", "mask", "metadata", "mpath", "path", "pattern", "polygon", "polyline", "radialGradient", "rect", "stop", "switch", "text", "textPath", "tspan", "use", "view"; optional):
    The component used to render a link when the `href` prop is
    provided.

- TouchRippleProps (boolean | number | string | dict | list; optional):
    Props applied to the `TouchRipple` element.

- about (string; optional)

- accessKey (string; optional)

- action (boolean | number | string | dict | list; optional):
    A ref for imperative actions. It currently only supports
    `focusVisible()` action.

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoFocus (boolean; optional):
    If `True`, the list item is focused during the first mount. Focus
    will also be triggered if the value changes from False to True.

- autoSave (string; optional)

- centerRipple (boolean; optional):
    If `True`, the ripples are centered. They won't start at the
    cursor interaction position.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- color (string; optional)

- contentEditable (a value equal to: false, true, "true", "false", "inherit"; optional)

- contextMenu (string; optional)

- dangerouslySetInnerHTML (boolean | number | string | dict | list; optional)

- datatype (string; optional)

- defaultChecked (boolean; optional)

- defaultValue (string | number | boolean | number | string | dict | list; optional)

- dense (boolean; optional):
    If `True`, compact vertical padding designed for keyboard and
    mouse input is used. The prop defaults to the value inherited from
    the parent Menu component.

- dir (string; optional)

- disableGutters (boolean; optional):
    If `True`, the left and right padding is removed.

- disableRipple (boolean; optional):
    If `True`, the ripple effect is disabled.  ⚠️ Without a ripple
    there is no styling for :focus-visible by default. Be sure to
    highlight the element by applying separate styles with the
    `.Mui-focusVisible` class.

- disableTouchRipple (boolean; optional):
    If `True`, the touch ripple effect is disabled.

- disabled (boolean; optional):
    If `True`, the component is disabled.

- divider (boolean; optional):
    If `True`, a 1px light border is added to the bottom of the menu
    item.

- download (boolean | number | string | dict | list; optional)

- draggable (a value equal to: false, true, "true", "false"; optional)

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

- hidden (boolean; optional)

- href (string; optional)

- hrefLang (string; optional)

- inlist (boolean | number | string | dict | list; optional)

- inputMode (a value equal to: "text", "none", "search", "tel", "url", "email", "numeric", "decimal"; optional):
    Hints at the type of data that might be entered by the user while
    editing the element or its contents.

- is (string; optional):
    Specify that a standard HTML element should behave like a defined
    custom built-in element.

- itemID (string; optional)

- itemProp (string; optional)

- itemRef (string; optional)

- itemScope (boolean; optional)

- itemType (string; optional)

- key (string | number; optional)

- lang (string; optional)

- media (string; optional)

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- ping (string; optional)

- placeholder (string; optional)

- prefix (string; optional)

- property (string; optional)

- radioGroup (string; optional)

- ref (boolean | number | string | dict | list; optional)

- referrerPolicy (a value equal to: "", "no-referrer", "no-referrer-when-downgrade", "origin", "origin-when-cross-origin", "same-origin", "strict-origin", "strict-origin-when-cross-origin", "unsafe-url"; optional)

- rel (string; optional)

- resource (string; optional)

- results (number; optional)

- role (string | a value equal to: "article", "button", "dialog", "figure", "form", "img", "link", "main", "menu", "menuitem", "option", "table", "switch", "alert", "alertdialog", "application", "banner", "cell", "checkbox", "columnheader", "combobox", "complementary", "contentinfo", "definition", "directory", "document", "feed", "grid", "gridcell", "group", "heading", "list", "listbox", "listitem", "log", "marquee", "math", "menubar", "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "tab", "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"; optional)

- security (string; optional)

- selected (boolean; optional):
    Use to apply selected styling.

- slot (string; optional)

- spellCheck (a value equal to: false, true, "true", "false"; optional)

- style (boolean | number | string | dict | list; optional)

- suppressContentEditableWarning (boolean; optional)

- suppressHydrationWarning (boolean; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- tabIndex (number; optional)

- target (string | a value equal to: "_self", "_blank", "_parent", "_top"; optional)

- title (string; optional)

- translate (a value equal to: "yes", "no"; optional)

- type (string; optional)

- typeof (string; optional)

- unselectable (a value equal to: "on", "off"; optional)

- value (string; default ''):
    The value represented by this menu item.

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'MenuItem'
    @_explicitize_args
    def __init__(self, children=None, href=Component.UNDEFINED, autoFocus=Component.UNDEFINED, classes=Component.UNDEFINED, dense=Component.UNDEFINED, disabled=Component.UNDEFINED, disableGutters=Component.UNDEFINED, divider=Component.UNDEFINED, selected=Component.UNDEFINED, sx=Component.UNDEFINED, tabIndex=Component.UNDEFINED, action=Component.UNDEFINED, centerRipple=Component.UNDEFINED, disableRipple=Component.UNDEFINED, disableTouchRipple=Component.UNDEFINED, focusRipple=Component.UNDEFINED, focusVisibleClassName=Component.UNDEFINED, LinkComponent=Component.UNDEFINED, TouchRippleProps=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, ref=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, key=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, download=Component.UNDEFINED, hrefLang=Component.UNDEFINED, media=Component.UNDEFINED, ping=Component.UNDEFINED, rel=Component.UNDEFINED, target=Component.UNDEFINED, type=Component.UNDEFINED, referrerPolicy=Component.UNDEFINED, value=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'LinkComponent', 'TouchRippleProps', 'about', 'accessKey', 'action', 'autoCapitalize', 'autoCorrect', 'autoFocus', 'autoSave', 'centerRipple', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dense', 'dir', 'disableGutters', 'disableRipple', 'disableTouchRipple', 'disabled', 'divider', 'download', 'draggable', 'focusRipple', 'focusVisibleClassName', 'hidden', 'href', 'hrefLang', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'key', 'lang', 'media', 'n_clicks', 'ping', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'referrerPolicy', 'rel', 'resource', 'results', 'role', 'security', 'selected', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'target', 'title', 'translate', 'type', 'typeof', 'unselectable', 'value', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'LinkComponent', 'TouchRippleProps', 'about', 'accessKey', 'action', 'autoCapitalize', 'autoCorrect', 'autoFocus', 'autoSave', 'centerRipple', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dense', 'dir', 'disableGutters', 'disableRipple', 'disableTouchRipple', 'disabled', 'divider', 'download', 'draggable', 'focusRipple', 'focusVisibleClassName', 'hidden', 'href', 'hrefLang', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'key', 'lang', 'media', 'n_clicks', 'ping', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'referrerPolicy', 'rel', 'resource', 'results', 'role', 'security', 'selected', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'target', 'title', 'translate', 'type', 'typeof', 'unselectable', 'value', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MenuItem, self).__init__(children=children, **args)
