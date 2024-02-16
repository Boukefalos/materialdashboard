# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Pagination(Component):
    """A Pagination component.
Material-UI Pagination.

Keyword arguments:

- id (string; optional)

- about (string; optional)

- accessKey (string; optional)

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoSave (string; optional)

- boundaryCount (number; optional):
    Number of always visible pages at the beginning and end.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- color (a value equal to: "standard", "primary", "secondary"; optional):
    The active color.

- componentName (string; optional):
    The name of the component where this hook is used.

- contentEditable (a value equal to: false, true, "true", "false", "inherit"; optional)

- contextMenu (string; optional)

- count (number; optional):
    The total number of pages.

- dangerouslySetInnerHTML (boolean | number | string | dict | list; optional)

- datatype (string; optional)

- defaultChecked (boolean; optional)

- defaultPage (number; optional):
    The page selected by default when the component is uncontrolled.

- defaultValue (string | number | boolean | number | string | dict | list; optional)

- dir (string; optional)

- disabled (boolean; optional):
    If `True`, the component is disabled.

- draggable (a value equal to: false, true, "true", "false"; optional)

- hidden (boolean; optional)

- hideNextButton (boolean; optional):
    If `True`, hide the next-page button.

- hidePrevButton (boolean; optional):
    If `True`, hide the previous-page button.

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

- page (number; optional):
    The current page.

- placeholder (string; optional)

- prefix (string; optional)

- property (string; optional)

- radioGroup (string; optional)

- ref (boolean | number | string | dict | list; optional)

- resource (string; optional)

- results (number; optional)

- role (string | a value equal to: "article", "button", "dialog", "figure", "form", "img", "link", "main", "menu", "menuitem", "option", "table", "switch", "alert", "alertdialog", "application", "banner", "cell", "checkbox", "columnheader", "combobox", "complementary", "contentinfo", "definition", "directory", "document", "feed", "grid", "gridcell", "group", "heading", "list", "listbox", "listitem", "log", "marquee", "math", "menubar", "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "tab", "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"; optional)

- security (string; optional)

- shape (a value equal to: "rounded", "circular"; optional):
    The shape of the pagination items.

- showFirstButton (boolean; optional):
    If `True`, show the first-page button.

- showLastButton (boolean; optional):
    If `True`, show the last-page button.

- siblingCount (number; optional):
    Number of always visible pages before and after the current page.

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

- variant (a value equal to: "text", "outlined"; optional):
    The variant to use.

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Pagination'
    @_explicitize_args
    def __init__(self, classes=Component.UNDEFINED, color=Component.UNDEFINED, shape=Component.UNDEFINED, size=Component.UNDEFINED, sx=Component.UNDEFINED, variant=Component.UNDEFINED, boundaryCount=Component.UNDEFINED, componentName=Component.UNDEFINED, count=Component.UNDEFINED, defaultPage=Component.UNDEFINED, disabled=Component.UNDEFINED, hideNextButton=Component.UNDEFINED, hidePrevButton=Component.UNDEFINED, page=Component.UNDEFINED, showFirstButton=Component.UNDEFINED, showLastButton=Component.UNDEFINED, siblingCount=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, ref=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoSave', 'boundaryCount', 'className', 'classes', 'color', 'componentName', 'contentEditable', 'contextMenu', 'count', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultPage', 'defaultValue', 'dir', 'disabled', 'draggable', 'hidden', 'hideNextButton', 'hidePrevButton', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'n_clicks', 'page', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'shape', 'showFirstButton', 'showLastButton', 'siblingCount', 'size', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'variant', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoSave', 'boundaryCount', 'className', 'classes', 'color', 'componentName', 'contentEditable', 'contextMenu', 'count', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultPage', 'defaultValue', 'dir', 'disabled', 'draggable', 'hidden', 'hideNextButton', 'hidePrevButton', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'n_clicks', 'page', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'shape', 'showFirstButton', 'showLastButton', 'siblingCount', 'size', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'variant', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Pagination, self).__init__(**args)
