# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Dialog(Component):
    """A Dialog component.
Material-UI Dialog.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Dialog children, usually the included sub-components.

- id (string; optional)

- BackdropComponent (a value equal to: "symbol" | a value equal to: "object" | a value equal to: "style" | a value equal to: "div" | a value equal to: "a" | a value equal to: "abbr" | a value equal to: "address" | a value equal to: "area" | a value equal to: "article" | a value equal to: "aside" | a value equal to: "audio" | a value equal to: "b" | a value equal to: "base" | a value equal to: "bdi" | a value equal to: "bdo" | a value equal to: "big" | a value equal to: "blockquote" | a value equal to: "body" | a value equal to: "br" | a value equal to: "button" | a value equal to: "canvas" | a value equal to: "caption" | a value equal to: "cite" | a value equal to: "code" | a value equal to: "col" | a value equal to: "colgroup" | a value equal to: "data" | a value equal to: "datalist" | a value equal to: "dd" | a value equal to: "del" | a value equal to: "details" | a value equal to: "dfn" | a value equal to: "dialog" | a value equal to: "dl" | a value equal to: "dt" | a value equal to: "em" | a value equal to: "embed" | a value equal to: "fieldset" | a value equal to: "figcaption" | a value equal to: "figure" | a value equal to: "footer" | a value equal to: "form" | a value equal to: "h1" | a value equal to: "h2" | a value equal to: "h3" | a value equal to: "h4" | a value equal to: "h5" | a value equal to: "h6" | a value equal to: "head" | a value equal to: "header" | a value equal to: "hgroup" | a value equal to: "hr" | a value equal to: "html" | a value equal to: "i" | a value equal to: "iframe" | a value equal to: "img" | a value equal to: "input" | a value equal to: "ins" | a value equal to: "kbd" | a value equal to: "keygen" | a value equal to: "label" | a value equal to: "legend" | a value equal to: "li" | a value equal to: "link" | a value equal to: "main" | a value equal to: "map" | a value equal to: "mark" | a value equal to: "menu" | a value equal to: "menuitem" | a value equal to: "meta" | a value equal to: "meter" | a value equal to: "nav" | a value equal to: "noindex" | a value equal to: "noscript" | a value equal to: "ol" | a value equal to: "optgroup" | a value equal to: "option" | a value equal to: "output" | a value equal to: "p" | a value equal to: "param" | a value equal to: "picture" | a value equal to: "pre" | a value equal to: "progress" | a value equal to: "q" | a value equal to: "rp" | a value equal to: "rt" | a value equal to: "ruby" | a value equal to: "s" | a value equal to: "samp" | a value equal to: "slot" | a value equal to: "script" | a value equal to: "section" | a value equal to: "select" | a value equal to: "small" | a value equal to: "source" | a value equal to: "span" | a value equal to: "strong" | a value equal to: "sub" | a value equal to: "summary" | a value equal to: "sup" | a value equal to: "table" | a value equal to: "template" | a value equal to: "tbody" | a value equal to: "td" | a value equal to: "textarea" | a value equal to: "tfoot" | a value equal to: "th" | a value equal to: "thead" | a value equal to: "time" | a value equal to: "title" | a value equal to: "tr" | a value equal to: "track" | a value equal to: "u" | a value equal to: "ul" | a value equal to: "var" | a value equal to: "video" | a value equal to: "wbr" | a value equal to: "webview" | a value equal to: "svg" | a value equal to: "animate" | a value equal to: "animateMotion" | a value equal to: "animateTransform" | a value equal to: "circle" | a value equal to: "clipPath" | a value equal to: "defs" | a value equal to: "desc" | a value equal to: "ellipse" | a value equal to: "feBlend" | a value equal to: "feColorMatrix" | a value equal to: "feComponentTransfer" | a value equal to: "feComposite" | a value equal to: "feConvolveMatrix" | a value equal to: "feDiffuseLighting" | a value equal to: "feDisplacementMap" | a value equal to: "feDistantLight" | a value equal to: "feDropShadow" | a value equal to: "feFlood" | a value equal to: "feFuncA" | a value equal to: "feFuncB" | a value equal to: "feFuncG" | a value equal to: "feFuncR" | a value equal to: "feGaussianBlur" | a value equal to: "feImage" | a value equal to: "feMerge" | a value equal to: "feMergeNode" | a value equal to: "feMorphology" | a value equal to: "feOffset" | a value equal to: "fePointLight" | a value equal to: "feSpecularLighting" | a value equal to: "feSpotLight" | a value equal to: "feTile" | a value equal to: "feTurbulence" | a value equal to: "filter" | a value equal to: "foreignObject" | a value equal to: "g" | a value equal to: "image" | a value equal to: "line" | a value equal to: "linearGradient" | a value equal to: "marker" | a value equal to: "mask" | a value equal to: "metadata" | a value equal to: "mpath" | a value equal to: "path" | a value equal to: "pattern" | a value equal to: "polygon" | a value equal to: "polyline" | a value equal to: "radialGradient" | a value equal to: "rect" | a value equal to: "stop" | a value equal to: "switch" | a value equal to: "text" | a value equal to: "textPath" | a value equal to: "tspan" | a value equal to: "use" | a value equal to: "view" | boolean | number | string | dict | list; optional):
    A backdrop component. This prop enables custom backdrop rendering.

- BackdropProps (boolean | number | string | dict | list; optional):
    Props applied to the [`Backdrop`](/api/backdrop/) element.   Props
    applied to the [`BackdropUnstyled`](/api/backdrop-unstyled/)
    element.

- PaperComponent (boolean | number | string | dict | list; optional):
    The component used to render the body of the dialog.

- PaperProps (boolean | number | string | dict | list; optional):
    Props applied to the [`Paper`](/api/paper/) element.

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

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoSave (string; optional)

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- closeAfterTransition (boolean; optional):
    When set to True the Modal waits until a nested Transition is
    completed before closing.

- color (string; optional)

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the Modal. Either a
    string to use a HTML element or a component.

- componentsProps (boolean | number | string | dict | list; optional):
    The props used for each slot inside the Modal.

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

- disableAutoFocus (boolean; optional):
    If `True`, the modal will not automatically shift focus to itself
    when it opens, and replace it to the last focused element when it
    closes. This also works correctly with any modal children that
    have the `disableAutoFocus` prop.  Generally this should never be
    set to `True` as it makes the modal less accessible to assistive
    technologies, like screen readers.

- disableEnforceFocus (boolean; optional):
    If `True`, the modal will not prevent focus from leaving the modal
    while open.  Generally this should never be set to `True` as it
    makes the modal less accessible to assistive technologies, like
    screen readers.

- disableEscapeKeyDown (boolean; optional):
    If `True`, hitting escape will not fire the `onClose` callback.

- disablePortal (boolean; optional):
    The `children` will be under the DOM hierarchy of the parent
    component.

- disableRestoreFocus (boolean; optional):
    If `True`, the modal will not restore focus to previously focused
    element once modal is hidden.

- disableScrollLock (boolean; optional):
    Disable the scroll lock behavior.

- draggable (a value equal to: false, true, "true", "false"; optional)

- fullScreen (boolean; optional):
    If `True`, the dialog is full-screen.

- fullWidth (boolean; optional):
    If `True`, the dialog stretches to `maxWidth`.  Notice that the
    dialog width grow is limited by the default margin.

- hidden (boolean; optional)

- hideBackdrop (boolean; optional):
    If `True`, the backdrop is not rendered.

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
    the Modal.

- key (string | number; optional)

- lang (string; optional)

- maxWidth (a value equal to: false, "xs", "sm", "md", "lg", "xl"; optional):
    Determine the max-width of the dialog. The dialog width grows with
    the size of the screen. Set to `False` to disable `maxWidth`.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- open (boolean; optional):
    If `True`, the component is shown.

- placeholder (string; optional)

- prefix (string; optional)

- property (string; optional)

- radioGroup (string; optional)

- ref (boolean | number | string | dict | list; optional)

- resource (string; optional)

- results (number; optional)

- role (string | a value equal to: "article", "button", "dialog", "figure", "form", "img", "link", "main", "menu", "menuitem", "option", "table", "switch", "alert", "alertdialog", "application", "banner", "cell", "checkbox", "columnheader", "combobox", "complementary", "contentinfo", "definition", "directory", "document", "feed", "grid", "gridcell", "group", "heading", "list", "listbox", "listitem", "log", "marquee", "math", "menubar", "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "tab", "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"; optional)

- scroll (a value equal to: "body", "paper"; optional):
    Determine the container for scrolling the dialog.

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
    _type = 'Dialog'
    @_explicitize_args
    def __init__(self, children=None, classes=Component.UNDEFINED, disableEscapeKeyDown=Component.UNDEFINED, fullScreen=Component.UNDEFINED, fullWidth=Component.UNDEFINED, maxWidth=Component.UNDEFINED, open=Component.UNDEFINED, PaperComponent=Component.UNDEFINED, PaperProps=Component.UNDEFINED, scroll=Component.UNDEFINED, sx=Component.UNDEFINED, TransitionComponent=Component.UNDEFINED, transitionDuration=Component.UNDEFINED, TransitionProps=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, ref=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, key=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, BackdropComponent=Component.UNDEFINED, BackdropProps=Component.UNDEFINED, closeAfterTransition=Component.UNDEFINED, container=Component.UNDEFINED, disableAutoFocus=Component.UNDEFINED, disableEnforceFocus=Component.UNDEFINED, disablePortal=Component.UNDEFINED, disableRestoreFocus=Component.UNDEFINED, disableScrollLock=Component.UNDEFINED, hideBackdrop=Component.UNDEFINED, keepMounted=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'BackdropComponent', 'BackdropProps', 'PaperComponent', 'PaperProps', 'TransitionComponent', 'TransitionProps', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'closeAfterTransition', 'color', 'components', 'componentsProps', 'container', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disableAutoFocus', 'disableEnforceFocus', 'disableEscapeKeyDown', 'disablePortal', 'disableRestoreFocus', 'disableScrollLock', 'draggable', 'fullScreen', 'fullWidth', 'hidden', 'hideBackdrop', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'keepMounted', 'key', 'lang', 'maxWidth', 'n_clicks', 'open', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'scroll', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'transitionDuration', 'translate', 'typeof', 'unselectable', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'BackdropComponent', 'BackdropProps', 'PaperComponent', 'PaperProps', 'TransitionComponent', 'TransitionProps', 'about', 'accessKey', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'closeAfterTransition', 'color', 'components', 'componentsProps', 'container', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disableAutoFocus', 'disableEnforceFocus', 'disableEscapeKeyDown', 'disablePortal', 'disableRestoreFocus', 'disableScrollLock', 'draggable', 'fullScreen', 'fullWidth', 'hidden', 'hideBackdrop', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'keepMounted', 'key', 'lang', 'maxWidth', 'n_clicks', 'open', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'scroll', 'security', 'slot', 'spellCheck', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'transitionDuration', 'translate', 'typeof', 'unselectable', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Dialog, self).__init__(children=children, **args)
