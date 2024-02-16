# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Rating(Component):
    """A Rating component.
Material-UI Rating.

Keyword arguments:

- id (string; optional)

- IconContainerComponent (boolean | number | string | dict | list | a value equal to: "object", "style", "div", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noindex", "noscript", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "slot", "script", "section", "select", "small", "source", "span", "strong", "sub", "summary", "sup", "table", "template", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr", "webview"; optional):
    The component containing the icon.

- about (string; optional)

- accessKey (string; optional)

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoSave (string; optional)

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- color (string; optional)

- contentEditable (a value equal to: false, true, "true", "false", "inherit"; optional)

- contextMenu (string; optional)

- dangerouslySetInnerHTML (boolean | number | string | dict | list; optional)

- datatype (string; optional)

- defaultChecked (boolean; optional)

- defaultValue (number; optional):
    The default value. Use when the component is not controlled.

- dir (string; optional)

- disabled (boolean; optional):
    If `True`, the component is disabled.

- draggable (a value equal to: false, true, "true", "false"; optional)

- emptyIcon (boolean | number | string | dict | list; optional):
    The icon to display when empty.

- emptyLabelText (boolean | number | string | dict | list; optional):
    The label read when the rating input is empty.

- hidden (boolean; optional)

- highlightSelectedOnly (boolean; optional):
    If `True`, only the selected icon will be highlighted.

- icon (boolean | number | string | dict | list; optional):
    The icon to display.

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

- lang (string; optional)

- max (number; optional):
    Maximum rating.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- name (string; optional):
    The name attribute of the radio `input` elements. This input
    `name` should be unique within the page. Being unique within a
    form is insufficient since the `name` is used to generated IDs.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose user interactions will persist after refreshing
    the  component or the page. Since only `value` is allowed this
    prop can normally be ignored.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when  the component - or the page - is refreshed. If `persisted`
    is truthy and  hasn't changed from its previous value, a `value`
    that the user has  changed while using the app will keep that
    change, as long as  the new `value` also matches what was given
    originally. Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory', 'location'; default 'local'):
    Where persisted user changes will be stored:  memory: only kept in
    memory, reset on page refresh.  local: window.localStorage, data
    is kept after the browser quit.  session: window.sessionStorage,
    data is cleared once the browser quit.  location: window.location,
    data appears in the URL and can be shared with others.

- placeholder (string; optional)

- precision (number; optional):
    The minimum increment value change allowed.

- prefix (string; optional)

- property (string; optional)

- radioGroup (string; optional)

- readOnly (boolean; optional):
    Removes all hover effects and pointer events.

- ref (boolean | number | string | dict | list; optional)

- resource (string; optional)

- results (number; optional)

- role (string | a value equal to: "article", "button", "dialog", "figure", "form", "img", "link", "main", "menu", "menuitem", "option", "table", "switch", "alert", "alertdialog", "application", "banner", "cell", "checkbox", "columnheader", "combobox", "complementary", "contentinfo", "definition", "directory", "document", "feed", "grid", "gridcell", "group", "heading", "list", "listbox", "listitem", "log", "marquee", "math", "menubar", "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "tab", "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"; optional)

- security (string; optional)

- size (a value equal to: "small", "medium", "large"; optional):
    The size of the component.

- slot (string; optional)

- spellCheck (a value equal to: false, true, "true", "false"; optional)

- style (boolean | number | string | dict | list; optional)

- suppressContentEditableWarning (boolean; optional)

- suppressHydrationWarning (boolean; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- tabIndex (number; optional)

- title (string; optional)

- translate (a value equal to: "yes", "no"; optional)

- typeof (string; optional)

- unselectable (a value equal to: "on", "off"; optional)

- value (number; optional):
    The rating value.

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Rating'
    @_explicitize_args
    def __init__(self, classes=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, emptyIcon=Component.UNDEFINED, emptyLabelText=Component.UNDEFINED, highlightSelectedOnly=Component.UNDEFINED, icon=Component.UNDEFINED, IconContainerComponent=Component.UNDEFINED, max=Component.UNDEFINED, name=Component.UNDEFINED, precision=Component.UNDEFINED, readOnly=Component.UNDEFINED, size=Component.UNDEFINED, sx=Component.UNDEFINED, value=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, ref=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'IconContainerComponent', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disabled', 'draggable', 'emptyIcon', 'emptyLabelText', 'hidden', 'highlightSelectedOnly', 'icon', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'max', 'n_clicks', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'precision', 'prefix', 'property', 'radioGroup', 'readOnly', 'ref', 'resource', 'results', 'role', 'security', 'size', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'value', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'IconContainerComponent', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disabled', 'draggable', 'emptyIcon', 'emptyLabelText', 'hidden', 'highlightSelectedOnly', 'icon', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'max', 'n_clicks', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'precision', 'prefix', 'property', 'radioGroup', 'readOnly', 'ref', 'resource', 'results', 'role', 'security', 'size', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'value', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Rating, self).__init__(**args)
