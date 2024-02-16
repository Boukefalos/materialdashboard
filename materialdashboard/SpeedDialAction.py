# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SpeedDialAction(Component):
    """A SpeedDialAction component.
Material-UI SpeedDialAction.

Keyword arguments:

- id (string; optional):
    This prop is used to help implement the accessibility logic. If
    you don't provide this prop. It falls back to a randomly generated
    id.

- FabProps (boolean | number | string | dict | list; optional):
    Props applied to the [`Fab`](/api/fab/) component.

- PopperComponent (boolean | number | string | dict | list; optional):
    The component used for the popper.

- PopperProps (boolean | number | string | dict | list; optional):
    Props applied to the [`Popper`](/api/popper/) element.

- TooltipClasses (boolean | number | string | dict | list; optional):
    `classes` prop applied to the [`Tooltip`](/api/tooltip/) element.

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

- arrow (boolean; optional):
    If `True`, adds an arrow to the tooltip.

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

- delay (number; optional):
    Adds a transition delay, to allow a series of SpeedDialActions to
    be animated.

- describeChild (boolean; optional):
    Set to `True` if the `title` acts as an accessible description. By
    default the `title` acts as an accessible label for the child.

- dir (string; optional)

- disableFocusListener (boolean; optional):
    Do not respond to focus-visible events.

- disableHoverListener (boolean; optional):
    Do not respond to hover events.

- disableInteractive (boolean; optional):
    Makes a tooltip not interactive, i.e. it will close when the user
    hovers over the tooltip before the `leaveDelay` is expired.

- disableTouchListener (boolean; optional):
    Do not respond to long press touch events.

- draggable (a value equal to: false, true, "true", "false"; optional)

- enterDelay (number; optional):
    The number of milliseconds to wait before showing the tooltip.
    This prop won't impact the enter touch delay (`enterTouchDelay`).

- enterNextDelay (number; optional):
    The number of milliseconds to wait before showing the tooltip when
    one was already recently opened.

- enterTouchDelay (number; optional):
    The number of milliseconds a user must touch the element before
    showing the tooltip.

- followCursor (boolean; optional):
    If `True`, the tooltip follow the cursor over the wrapped element.

- hidden (boolean; optional)

- icon (boolean | number | string | dict | list; optional):
    The icon to display in the SpeedDial Fab.

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

- leaveDelay (number; optional):
    The number of milliseconds to wait before hiding the tooltip. This
    prop won't impact the leave touch delay (`leaveTouchDelay`).

- leaveTouchDelay (number; optional):
    The number of milliseconds after the user stops touching an
    element before hiding the tooltip.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- open (boolean; optional):
    If `True`, the component is shown.

- placeholder (string; optional)

- placement (a value equal to: "bottom", "left", "right", "top", "top-start", "top-end", "bottom-start", "bottom-end", "right-start", "right-end", "left-start", "left-end"; optional):
    Tooltip placement.

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

- title (boolean | number | string | dict | list; optional):
    Tooltip title. Zero-length titles string are never displayed.

- tooltipOpen (boolean; optional):
    Make the tooltip always visible when the SpeedDial is open.

- tooltipPlacement (a value equal to: "bottom", "left", "right", "top", "top-start", "top-end", "bottom-start", "bottom-end", "right-start", "right-end", "left-start", "left-end"; optional):
    Placement of the tooltip.

- tooltipTitle (boolean | number | string | dict | list; optional):
    Label to display in the tooltip.

- translate (a value equal to: "yes", "no"; optional)

- typeof (string; optional)

- unselectable (a value equal to: "on", "off"; optional)

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'SpeedDialAction'
    @_explicitize_args
    def __init__(self, classes=Component.UNDEFINED, FabProps=Component.UNDEFINED, delay=Component.UNDEFINED, icon=Component.UNDEFINED, sx=Component.UNDEFINED, TooltipClasses=Component.UNDEFINED, tooltipPlacement=Component.UNDEFINED, tooltipTitle=Component.UNDEFINED, tooltipOpen=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, ref=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, open=Component.UNDEFINED, TransitionComponent=Component.UNDEFINED, TransitionProps=Component.UNDEFINED, placement=Component.UNDEFINED, arrow=Component.UNDEFINED, describeChild=Component.UNDEFINED, disableFocusListener=Component.UNDEFINED, disableHoverListener=Component.UNDEFINED, disableInteractive=Component.UNDEFINED, disableTouchListener=Component.UNDEFINED, enterDelay=Component.UNDEFINED, enterNextDelay=Component.UNDEFINED, enterTouchDelay=Component.UNDEFINED, followCursor=Component.UNDEFINED, leaveDelay=Component.UNDEFINED, leaveTouchDelay=Component.UNDEFINED, PopperComponent=Component.UNDEFINED, PopperProps=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'FabProps', 'PopperComponent', 'PopperProps', 'TooltipClasses', 'TransitionComponent', 'TransitionProps', 'about', 'accessKey', 'arrow', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'delay', 'describeChild', 'dir', 'disableFocusListener', 'disableHoverListener', 'disableInteractive', 'disableTouchListener', 'draggable', 'enterDelay', 'enterNextDelay', 'enterTouchDelay', 'followCursor', 'hidden', 'icon', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'leaveDelay', 'leaveTouchDelay', 'n_clicks', 'open', 'placeholder', 'placement', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'tooltipOpen', 'tooltipPlacement', 'tooltipTitle', 'translate', 'typeof', 'unselectable', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'FabProps', 'PopperComponent', 'PopperProps', 'TooltipClasses', 'TransitionComponent', 'TransitionProps', 'about', 'accessKey', 'arrow', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'delay', 'describeChild', 'dir', 'disableFocusListener', 'disableHoverListener', 'disableInteractive', 'disableTouchListener', 'draggable', 'enterDelay', 'enterNextDelay', 'enterTouchDelay', 'followCursor', 'hidden', 'icon', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'leaveDelay', 'leaveTouchDelay', 'n_clicks', 'open', 'placeholder', 'placement', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'tooltipOpen', 'tooltipPlacement', 'tooltipTitle', 'translate', 'typeof', 'unselectable', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(SpeedDialAction, self).__init__(**args)
