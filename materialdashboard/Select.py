# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Select(Component):
    """A Select component.
Material-UI Select.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The option elements to populate the select with. Can be some
    `MenuItem` when `native` is False and `option` when `native` is
    True.  ⚠️The `MenuItem` elements **must** be direct descendants
    when `native` is False.

- id (string; optional):
    The `id` of the wrapper element or the `select` element when
    `native`.

- IconComponent (boolean | number | string | dict | list | a value equal to: "symbol", "object", "style", "div", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noindex", "noscript", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "slot", "script", "section", "select", "small", "source", "span", "strong", "sub", "summary", "sup", "table", "template", "tbody", "td", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr", "webview", "svg", "animate", "animateMotion", "animateTransform", "circle", "clipPath", "defs", "desc", "ellipse", "feBlend", "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow", "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur", "feImage", "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight", "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence", "filter", "foreignObject", "g", "image", "line", "linearGradient", "marker", "mask", "metadata", "mpath", "path", "pattern", "polygon", "polyline", "radialGradient", "rect", "stop", "switch", "text", "textPath", "tspan", "use", "view"; optional):
    The icon that displays the arrow.

- MenuProps (boolean | number | string | dict | list; optional):
    Props applied to the [`Menu`](/api/menu/) element.

- SelectDisplayProps (boolean | number | string | dict | list; optional):
    Props applied to the clickable div element.

- about (string; optional)

- accessKey (string; optional)

- autoCapitalize (string; optional)

- autoComplete (string; optional):
    This prop helps users to fill forms faster, especially on mobile
    devices. The name can be confusing, as it's more like an autofill.
    You can learn more about it [following the
    specification](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill).

- autoCorrect (string; optional)

- autoFocus (boolean; optional):
    If `True`, the `input` element is focused during the first mount.

- autoSave (string; optional)

- autoWidth (boolean; optional):
    If `True`, the width of the popover will automatically be set
    according to the items inside the menu, otherwise it will be at
    least the width of the select input.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- color (a value equal to: "success", "info", "warning", "error", "primary", "secondary"; optional):
    The color of the component. It supports those theme colors that
    make sense for this component. The prop defaults to the value
    (`'primary'`) inherited from the parent FormControl component.

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the InputBase. Either a
    string to use a HTML element or a component.

- componentsProps (boolean | number | string | dict | list; optional):
    The props used for each slot inside the Input.

- contentEditable (a value equal to: false, true, "true", "false", "inherit"; optional)

- contextMenu (string; optional)

- dangerouslySetInnerHTML (boolean | number | string | dict | list; optional)

- datatype (string; optional)

- defaultChecked (boolean; optional)

- dir (string; optional)

- disableUnderline (boolean; optional):
    If `True`, the `input` will not have an underline.

- disabled (boolean; optional):
    If `True`, the component is disabled. The prop defaults to the
    value (`False`) inherited from the parent FormControl component.

- displayEmpty (boolean; optional):
    If `True`, a value is displayed even if no items are selected.  In
    order to display a meaningful value, a function can be passed to
    the `renderValue` prop which returns the value to be displayed
    when no items are selected.  ⚠️ When using this prop, make sure
    the label doesn't overlap with the empty displayed value. The
    label should either be hidden or forced to a shrunk state.

- draggable (a value equal to: false, true, "true", "false"; optional)

- endAdornment (boolean | number | string | dict | list; optional):
    End `InputAdornment` for this component.

- error (boolean; optional):
    If `True`, the `input` will indicate an error. The prop defaults
    to the value (`False`) inherited from the parent FormControl
    component.

- fullWidth (boolean; optional):
    If `True`, the `input` will take up the full width of its
    container.

- hidden (boolean; optional)

- inlist (boolean | number | string | dict | list; optional)

- input (boolean | number | string | dict | list; optional):
    An `Input` element; does not have to be a material-ui specific
    `Input`.

- inputComponent (boolean | number | string | dict | list | a value equal to: "abbr", "address", "article", "aside", "b", "bdi", "bdo", "big", "blockquote", "caption", "cite", "code", "data", "dd", "del", "details", "dfn", "dt", "em", "figcaption", "figure", "footer", "head", "header", "hgroup", "i", "input", "kbd", "keygen", "main", "mark", "menu", "menuitem", "meter", "nav", "noindex", "noscript", "output", "picture", "rp", "rt", "ruby", "s", "samp", "section", "small", "span", "strong", "sub", "summary", "sup", "textarea", "time", "u", "var", "wbr", "webview"; optional):
    The component used for the `input` element. Either a string to use
    a HTML element or a component.

- inputMode (a value equal to: "text", "none", "search", "tel", "url", "email", "numeric", "decimal"; optional):
    Hints at the type of data that might be entered by the user while
    editing the element or its contents.

- inputProps (boolean | number | string | dict | list; optional):
    [Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#Attributes)
    applied to the `input` element. When `native` is `True`, the
    attributes are applied on the `select` element.

- inputRef (boolean | number | string | dict | list; optional):
    Pass a ref to the `input` element.

- is (string; optional):
    Specify that a standard HTML element should behave like a defined
    custom built-in element.

- itemID (string; optional)

- itemProp (string; optional)

- itemRef (string; optional)

- itemScope (boolean; optional)

- itemType (string; optional)

- label (boolean | number | string | dict | list; optional):
    See [OutlinedInput#label](/api/outlined-input/#props).

- labelId (string; optional):
    The ID of an element that acts as an additional label. The Select
    will be labelled by the additional label and the selected value.

- lang (string; optional)

- margin (a value equal to: "none", "dense"; optional):
    If `dense`, will adjust vertical spacing. This is normally
    obtained via context from FormControl. The prop defaults to the
    value (`'none'`) inherited from the parent FormControl component.

- maxRows (string | number; optional):
    Maximum number of rows to display when multiline option is set to
    True.

- minRows (string | number; optional):
    Minimum number of rows to display when multiline option is set to
    True.

- multiline (boolean; optional):
    If `True`, a `textarea` element is rendered.

- multiple (boolean; optional):
    If `True`, `value` must be an array and the menu will support
    multiple selections.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- name (string; optional):
    Name attribute of the `input` element.

- native (boolean; optional):
    If `True`, the component uses a native `select` element.

- open (boolean; optional):
    If `True`, the component is shown. You can only use it when the
    `native` prop is `False` (default).

- options (dict; optional):
    The options to present, where keys are the 'value' and the values
    will be displayed as menu items.

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

- placeholder (string; optional):
    The short hint displayed in the `input` before the user enters a
    value.

- prefix (string; optional)

- property (string; optional)

- radioGroup (string; optional)

- readOnly (boolean; optional):
    It prevents the user from changing the value of the field (not
    from interacting with the field).

- ref (boolean | number | string | dict | list; optional)

- required (boolean; optional):
    If `True`, the `input` element is required. The prop defaults to
    the value (`False`) inherited from the parent FormControl
    component.

- resource (string; optional)

- results (number; optional)

- role (string | a value equal to: "article", "button", "dialog", "figure", "form", "img", "link", "main", "menu", "menuitem", "option", "table", "switch", "alert", "alertdialog", "application", "banner", "cell", "checkbox", "columnheader", "combobox", "complementary", "contentinfo", "definition", "directory", "document", "feed", "grid", "gridcell", "group", "heading", "list", "listbox", "listitem", "log", "marquee", "math", "menubar", "menuitemcheckbox", "menuitemradio", "navigation", "none", "note", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "tab", "tablist", "tabpanel", "term", "textbox", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"; optional)

- rows (string | number; optional):
    Number of rows to display when multiline option is set to True.

- security (string; optional)

- size (a value equal to: "small", "medium"; optional):
    The size of the component.

- slot (string; optional)

- spellCheck (a value equal to: false, true, "true", "false"; optional)

- startAdornment (boolean | number | string | dict | list; optional):
    Start `InputAdornment` for this component.

- style (boolean | number | string | dict | list; optional)

- suppressContentEditableWarning (boolean; optional)

- suppressHydrationWarning (boolean; optional)

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- tabIndex (number; optional)

- title (string; optional)

- translate (a value equal to: "yes", "no"; optional)

- type (string; optional):
    Type of the `input` element. It should be [a valid HTML5 input
    type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#Form_%3Cinput%3E_types).

- typeof (string; optional)

- unselectable (a value equal to: "on", "off"; optional)

- value (string; default ''):
    The `input` value. Providing an empty string will select no
    options. Set to an empty string `''` if you don't want any of the
    available options to be selected.

- variant (a value equal to: "outlined", "standard", "filled"; optional):
    The variant to use.

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Select'

    @_explicitize_args
    def __init__(
            self, children=None, autoWidth=Component.UNDEFINED, classes=Component.UNDEFINED,
            displayEmpty=Component.UNDEFINED, IconComponent=Component.UNDEFINED, id=Component.UNDEFINED,
            input=Component.UNDEFINED, inputProps=Component.UNDEFINED, label=Component.UNDEFINED,
            labelId=Component.UNDEFINED, MenuProps=Component.UNDEFINED, multiple=Component.UNDEFINED,
            native=Component.UNDEFINED, open=Component.UNDEFINED, SelectDisplayProps=Component.UNDEFINED,
            sx=Component.UNDEFINED, variant=Component.UNDEFINED, className=Component.UNDEFINED,
            style=Component.UNDEFINED, ref=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED,
            defaultChecked=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED,
            suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED,
            contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED,
            draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, lang=Component.UNDEFINED,
            placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED,
            translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED,
            about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED,
            prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED,
            typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED,
            autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED,
            itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED,
            itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED,
            security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED,
            dangerouslySetInnerHTML=Component.UNDEFINED, margin=Component.UNDEFINED, disabled=Component.UNDEFINED,
            type=Component.UNDEFINED, error=Component.UNDEFINED, name=Component.UNDEFINED,
            autoFocus=Component.UNDEFINED, autoComplete=Component.UNDEFINED, readOnly=Component.UNDEFINED,
            required=Component.UNDEFINED, size=Component.UNDEFINED, rows=Component.UNDEFINED,
            fullWidth=Component.UNDEFINED, endAdornment=Component.UNDEFINED, components=Component.UNDEFINED,
            componentsProps=Component.UNDEFINED, inputRef=Component.UNDEFINED, inputComponent=Component.UNDEFINED,
            multiline=Component.UNDEFINED, maxRows=Component.UNDEFINED, minRows=Component.UNDEFINED,
            startAdornment=Component.UNDEFINED, disableUnderline=Component.UNDEFINED, persistence=Component.UNDEFINED,
            persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, value=Component.UNDEFINED,
            options=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs
    ):
        self._prop_names = ['children', 'id', 'IconComponent', 'MenuProps', 'SelectDisplayProps', 'about', 'accessKey',
                            'autoCapitalize', 'autoComplete', 'autoCorrect', 'autoFocus', 'autoSave', 'autoWidth',
                            'className', 'classes', 'color', 'components', 'componentsProps', 'contentEditable',
                            'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'dir',
                            'disableUnderline', 'disabled', 'displayEmpty', 'draggable', 'endAdornment', 'error',
                            'fullWidth', 'hidden', 'inlist', 'input', 'inputComponent', 'inputMode', 'inputProps',
                            'inputRef', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'label',
                            'labelId', 'lang', 'margin', 'maxRows', 'minRows', 'multiline', 'multiple', 'n_clicks',
                            'name', 'native', 'open', 'options', 'persisted_props', 'persistence', 'persistence_type',
                            'placeholder', 'prefix', 'property', 'radioGroup', 'readOnly', 'ref', 'required',
                            'resource', 'results', 'role', 'rows', 'security', 'size', 'slot', 'spellCheck',
                            'startAdornment', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning',
                            'sx', 'tabIndex', 'title', 'translate', 'type', 'typeof', 'unselectable', 'value',
                            'variant', 'vocab']
        self._valid_wildcard_attributes = []
        self.available_properties = ['children', 'id', 'IconComponent', 'MenuProps', 'SelectDisplayProps', 'about',
                                     'accessKey', 'autoCapitalize', 'autoComplete', 'autoCorrect', 'autoFocus',
                                     'autoSave', 'autoWidth', 'className', 'classes', 'color', 'components',
                                     'componentsProps', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML',
                                     'datatype', 'defaultChecked', 'dir', 'disableUnderline', 'disabled',
                                     'displayEmpty', 'draggable', 'endAdornment', 'error', 'fullWidth', 'hidden',
                                     'inlist', 'input', 'inputComponent', 'inputMode', 'inputProps', 'inputRef', 'is',
                                     'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'label', 'labelId',
                                     'lang', 'margin', 'maxRows', 'minRows', 'multiline', 'multiple', 'n_clicks',
                                     'name', 'native', 'open', 'options', 'persisted_props', 'persistence',
                                     'persistence_type', 'placeholder', 'prefix', 'property', 'radioGroup', 'readOnly',
                                     'ref', 'required', 'resource', 'results', 'role', 'rows', 'security', 'size',
                                     'slot', 'spellCheck', 'startAdornment', 'style', 'suppressContentEditableWarning',
                                     'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'type',
                                     'typeof', 'unselectable', 'value', 'variant', 'vocab']
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Select, self).__init__(children=children, **args)
