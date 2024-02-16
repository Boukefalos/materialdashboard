# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MenuList(Component):
    """A MenuList component.
Material-UI MenuList.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    MenuList contents, normally `MenuItem`s.

- id (string; optional)

- about (string; optional)

- accessKey (string; optional)

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoFocus (boolean; optional):
    If `True`, will focus the `[role=\"menu\"]` container and move
    into tab order.

- autoFocusItem (boolean; optional):
    If `True`, will focus the first menuitem if `variant=\"menu\"` or
    selected item if `variant=\"selectedMenu\"`.

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

- defaultValue (string | number | boolean | number | string | dict | list; optional)

- dense (boolean; optional):
    If `True`, compact vertical padding designed for keyboard and
    mouse input is used for the list and list items. The prop is
    available to descendant components as the `dense` context.

- dir (string; optional)

- disableListWrap (boolean; optional):
    If `True`, the menu items will not wrap focus.

- disablePadding (boolean; optional):
    If `True`, vertical padding is removed from the list.

- disabledItemsFocusable (boolean; optional):
    If `True`, will allow focus on disabled items.

- draggable (a value equal to: false, true, "true", "false"; optional)

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

- key (string | number; optional)

- lang (string; optional)

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- placeholder (string; optional)

- prefix (string; optional)

- property (string; optional)

- radioGroup (string; optional)

- ref (boolean | number | string | dict | list; optional)

- resource (string; optional)

- results (number; optional)

- role (string | a value equal to: "article", "button", "dialog", "figure", "form", "img", "link", "main", "menu", "menuitem", "option", "table", "switch", "alert", "alertdialog", "application", "banner", "cell", "checkbox", "columnheader", "combobox", "complementary", "contentinfo", "definition", "directory", "document", "feed", "grid", "gridcell", "group", "heading", "list", "listbox", "listitem", "log", "marquee", "math", "menubar", "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "tab", "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"; optional)

- security (string; optional)

- slot (string; optional)

- spellCheck (a value equal to: false, true, "true", "false"; optional)

- style (boolean | number | string | dict | list; optional)

- subheader (boolean | number | string | dict | list; optional):
    The content of the subheader, normally `ListSubheader`.

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

- variant (a value equal to: "menu", "selectedMenu"; optional):
    The variant to use. Use `menu` to prevent selected items from
    impacting the initial focus and the vertical alignment relative to
    the anchor element.

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'MenuList'
    @_explicitize_args
    def __init__(self, children=None, autoFocus=Component.UNDEFINED, autoFocusItem=Component.UNDEFINED, disabledItemsFocusable=Component.UNDEFINED, disableListWrap=Component.UNDEFINED, variant=Component.UNDEFINED, classes=Component.UNDEFINED, dense=Component.UNDEFINED, disablePadding=Component.UNDEFINED, subheader=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, ref=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, key=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoFocus', 'autoFocusItem', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dense', 'dir', 'disableListWrap', 'disablePadding', 'disabledItemsFocusable', 'draggable', 'hidden', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'key', 'lang', 'n_clicks', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'subheader', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'variant', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoFocus', 'autoFocusItem', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dense', 'dir', 'disableListWrap', 'disablePadding', 'disabledItemsFocusable', 'draggable', 'hidden', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'key', 'lang', 'n_clicks', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'subheader', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'variant', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MenuList, self).__init__(children=children, **args)
