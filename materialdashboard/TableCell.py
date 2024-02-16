# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TableCell(Component):
    """A TableCell component.
Material-UI TableCell.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional)

- abbr (string; optional)

- about (string; optional)

- accessKey (string; optional)

- align (a value equal to: "inherit", "left", "right", "center", "justify"; optional):
    Set the text-align on the table cell content.  Monetary or
    generally number fields **should be right aligned** as that allows
    you to add them up quickly in your head without having to worry
    about decimals.

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoSave (string; optional)

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- colSpan (number; optional)

- color (string; optional)

- component (boolean | number | string | dict | list | a value equal to: "div", "abbr", "address", "article", "aside", "b", "bdi", "bdo", "big", "blockquote", "caption", "cite", "code", "dd", "del", "details", "dfn", "dt", "em", "figcaption", "figure", "footer", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "i", "kbd", "keygen", "main", "mark", "menu", "menuitem", "meter", "nav", "noindex", "noscript", "output", "p", "picture", "rp", "rt", "ruby", "s", "samp", "section", "small", "span", "strong", "sub", "summary", "sup", "td", "th", "time", "u", "var", "wbr", "webview"; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- contentEditable (a value equal to: false, true, "true", "false", "inherit"; optional)

- contextMenu (string; optional)

- dangerouslySetInnerHTML (boolean | number | string | dict | list; optional)

- datatype (string; optional)

- defaultChecked (boolean; optional)

- defaultValue (string | number | boolean | number | string | dict | list; optional)

- dir (string; optional)

- draggable (a value equal to: false, true, "true", "false"; optional)

- headers (string; optional)

- height (string | number; optional)

- hidden (boolean; optional)

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

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- padding (a value equal to: "checkbox", "none", "normal"; optional):
    Sets the padding applied to the cell. The prop defaults to the
    value (`'default'`) inherited from the parent Table component.

- placeholder (string; optional)

- prefix (string; optional)

- property (string; optional)

- radioGroup (string; optional)

- ref (boolean | number | string | dict | list; optional)

- resource (string; optional)

- results (number; optional)

- role (string | a value equal to: "article", "button", "dialog", "figure", "form", "img", "link", "main", "menu", "menuitem", "option", "table", "switch", "alert", "alertdialog", "application", "banner", "cell", "checkbox", "columnheader", "combobox", "complementary", "contentinfo", "definition", "directory", "document", "feed", "grid", "gridcell", "group", "heading", "list", "listbox", "listitem", "log", "marquee", "math", "menubar", "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "tab", "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"; optional)

- rowSpan (number; optional)

- scope (string; optional):
    Set scope attribute.

- security (string; optional)

- size (a value equal to: "small", "medium"; optional):
    Specify the size of the cell. The prop defaults to the value
    (`'medium'`) inherited from the parent Table component.

- slot (string; optional)

- sortDirection (a value equal to: false, "desc", "asc"; optional):
    Set aria-sort direction.

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

- valign (a value equal to: "bottom", "top", "baseline", "middle"; optional)

- variant (a value equal to: "body", "footer", "head"; optional):
    Specify the cell type. The prop defaults to the value inherited
    from the parent TableHead, TableBody, or TableFooter components.

- vocab (string; optional)

- width (string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'TableCell'
    @_explicitize_args
    def __init__(self, children=None, align=Component.UNDEFINED, classes=Component.UNDEFINED, component=Component.UNDEFINED, padding=Component.UNDEFINED, scope=Component.UNDEFINED, size=Component.UNDEFINED, sortDirection=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, abbr=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, height=Component.UNDEFINED, width=Component.UNDEFINED, colSpan=Component.UNDEFINED, headers=Component.UNDEFINED, rowSpan=Component.UNDEFINED, valign=Component.UNDEFINED, ref=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'abbr', 'about', 'accessKey', 'align', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'colSpan', 'color', 'component', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'draggable', 'headers', 'height', 'hidden', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'n_clicks', 'padding', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'rowSpan', 'scope', 'security', 'size', 'slot', 'sortDirection', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'valign', 'variant', 'vocab', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'abbr', 'about', 'accessKey', 'align', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'colSpan', 'color', 'component', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'draggable', 'headers', 'height', 'hidden', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'n_clicks', 'padding', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'rowSpan', 'scope', 'security', 'size', 'slot', 'sortDirection', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'valign', 'variant', 'vocab', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(TableCell, self).__init__(children=children, **args)
