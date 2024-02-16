# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Popper(Component):
    """A Popper component.
Material-UI Popper.

Keyword arguments:

- children (string | number | boolean | number | string | dict | list | a value equal to: false, true; optional):
    Popper render function or node.

- id (string; optional)

- about (string; optional)

- accessKey (string; optional)

- anchorEl (string; optional):
    An HTML element,
    [virtualElement](https://popper.js.org/docs/v2/virtual-elements/),
    or a function that returns either. It's used to set the position
    of the popper. The return value will passed as the reference
    object of the Popper instance. If specified, the ID of an existing
    element should be provided.

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoSave (string; optional)

- className (string; optional)

- color (string; optional)

- container (string; optional):
    An HTML element or function that returns one. The `container` will
    have the portal children appended to it.  By default, it uses the
    body of the top-level document object, so it's simply
    `document.body` most of the time. If specified, the ID of an
    existing element should be provided.

- contentEditable (a value equal to: false, true, "true", "false", "inherit"; optional)

- contextMenu (string; optional)

- dangerouslySetInnerHTML (boolean | number | string | dict | list; optional)

- datatype (string; optional)

- defaultChecked (boolean; optional)

- defaultValue (string | number | boolean | number | string | dict | list; optional)

- dir (string; optional)

- disablePortal (boolean; optional):
    The `children` will be under the DOM hierarchy of the parent
    component.

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

- keepMounted (boolean; optional):
    Always keep the children in the DOM. This prop can be useful in
    SEO situation or when you want to maximize the responsiveness of
    the Popper.

- lang (string; optional)

- modifiers (list of boolean | number | string | dict | lists; optional):
    Popper.js is based on a \"plugin-like\" architecture, most of its
    features are fully encapsulated \"modifiers\".  A modifier is a
    function that is called each time Popper.js needs to compute the
    position of the popper. For this reason, modifiers should be very
    performant to avoid bottlenecks. To learn how to create a
    modifier, [read the modifiers
    documentation](https://popper.js.org/docs/v2/modifiers/).

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- open (boolean; optional):
    If `True`, the component is shown.

- placeholder (string; optional)

- placement (a value equal to: "bottom", "left", "right", "top", "auto", "auto-start", "auto-end", "top-start", "top-end", "bottom-start", "bottom-end", "right-start", "right-end", "left-start", "left-end"; optional):
    Popper placement.

- popperOptions (boolean | number | string | dict | list; optional):
    Options provided to the
    [`Popper.js`](https://popper.js.org/docs/v2/constructors/#options)
    instance.

- popperRef (boolean | number | string | dict | list; optional):
    A ref that points to the used popper instance.

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

- suppressContentEditableWarning (boolean; optional)

- suppressHydrationWarning (boolean; optional)

- tabIndex (number; optional)

- title (string; optional)

- transition (boolean; optional):
    Help supporting a react-transition-group/Transition component.

- translate (a value equal to: "yes", "no"; optional)

- typeof (string; optional)

- unselectable (a value equal to: "on", "off"; optional)

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Popper'
    @_explicitize_args
    def __init__(self, children=None, ref=Component.UNDEFINED, anchorEl=Component.UNDEFINED, container=Component.UNDEFINED, disablePortal=Component.UNDEFINED, keepMounted=Component.UNDEFINED, modifiers=Component.UNDEFINED, open=Component.UNDEFINED, placement=Component.UNDEFINED, popperOptions=Component.UNDEFINED, popperRef=Component.UNDEFINED, transition=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'about', 'accessKey', 'anchorEl', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'color', 'container', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disablePortal', 'draggable', 'hidden', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'keepMounted', 'lang', 'modifiers', 'n_clicks', 'open', 'placeholder', 'placement', 'popperOptions', 'popperRef', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'tabIndex', 'title', 'transition', 'translate', 'typeof', 'unselectable', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'about', 'accessKey', 'anchorEl', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'color', 'container', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disablePortal', 'draggable', 'hidden', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'keepMounted', 'lang', 'modifiers', 'n_clicks', 'open', 'placeholder', 'placement', 'popperOptions', 'popperRef', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'tabIndex', 'title', 'transition', 'translate', 'typeof', 'unselectable', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Popper, self).__init__(children=children, **args)
