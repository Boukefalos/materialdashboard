# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SpeedDial(Component):
    """A SpeedDial component.
Material-UI SpeedDial.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    SpeedDialActions to display when the SpeedDial is `open`.

- id (string; optional)

- FabProps (boolean | number | string | dict | list; optional):
    Props applied to the [`Fab`](/api/fab/) element.

- TransitionComponent (boolean | number | string | dict | list; optional):
    The component used for the transition. [Follow this
    guide](/components/transitions/#transitioncomponent-prop) to learn
    more about the requirements for this component.

- TransitionProps (boolean | number | string | dict | list; optional):
    Props applied to the transition element. By default, the element
    is based on this
    [`Transition`](https://reactcommunity.org/react-transition-group/transition)
    component.

- about (string; optional)

- accessKey (string; optional)

- ariaLabel (string; optional):
    The aria-label of the button element. Also used to provide the
    `id` for the `SpeedDial` element and its children.

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

- defaultValue (string | number | boolean | number | string | dict | list; optional)

- dir (string; optional)

- direction (a value equal to: "left", "right", "up", "down"; optional):
    The direction the actions open relative to the floating action
    button.

- draggable (a value equal to: false, true, "true", "false"; optional)

- hidden (boolean; optional):
    If `True`, the SpeedDial is hidden.

- icon (boolean | number | string | dict | list; optional):
    The icon to display in the SpeedDial Fab. The `SpeedDialIcon`
    component provides a default Icon with animation.

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

- open (boolean; optional):
    If `True`, the component is shown.

- openIcon (boolean | number | string | dict | list; optional):
    The icon to display in the SpeedDial Fab when the SpeedDial is
    open.

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

- suppressContentEditableWarning (boolean; optional)

- suppressHydrationWarning (boolean; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- tabIndex (number; optional)

- title (string; optional)

- transitionDuration (number | boolean | number | string | dict | list; optional):
    The duration for the transition, in milliseconds. You may specify
    a single timeout for all transitions, or individually with an
    object.

- translate (a value equal to: "yes", "no"; optional)

- typeof (string; optional)

- unselectable (a value equal to: "on", "off"; optional)

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'SpeedDial'
    @_explicitize_args
    def __init__(self, children=None, classes=Component.UNDEFINED, ariaLabel=Component.UNDEFINED, direction=Component.UNDEFINED, hidden=Component.UNDEFINED, FabProps=Component.UNDEFINED, icon=Component.UNDEFINED, open=Component.UNDEFINED, openIcon=Component.UNDEFINED, sx=Component.UNDEFINED, TransitionComponent=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, TransitionProps=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, ref=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'FabProps', 'TransitionComponent', 'TransitionProps', 'about', 'accessKey', 'ariaLabel', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'direction', 'draggable', 'hidden', 'icon', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'n_clicks', 'open', 'openIcon', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'transitionDuration', 'translate', 'typeof', 'unselectable', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'FabProps', 'TransitionComponent', 'TransitionProps', 'about', 'accessKey', 'ariaLabel', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'direction', 'draggable', 'hidden', 'icon', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'n_clicks', 'open', 'openIcon', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'transitionDuration', 'translate', 'typeof', 'unselectable', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(SpeedDial, self).__init__(children=children, **args)
