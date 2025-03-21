# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Input(Component):
    """An Input component.
Material-UI Input.

Keyword arguments:

- id (string; optional):
    The id of the `input` element.

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

- defaultValue (boolean | number | string | dict | list; optional):
    The default value. Use when the component is not controlled.

- dir (string; optional)

- disableUnderline (boolean; optional):
    If `True`, the `input` will not have an underline.

- disabled (boolean; optional):
    If `True`, the component is disabled. The prop defaults to the
    value (`False`) inherited from the parent FormControl component.

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

- inputComponent (boolean | number | string | dict | list | a value equal to: "abbr", "address", "article", "aside", "b", "bdi", "bdo", "big", "blockquote", "caption", "cite", "code", "data", "dd", "del", "details", "dfn", "dt", "em", "figcaption", "figure", "footer", "head", "header", "hgroup", "i", "input", "kbd", "keygen", "main", "mark", "menu", "menuitem", "meter", "nav", "noindex", "noscript", "output", "picture", "rp", "rt", "ruby", "s", "samp", "section", "small", "span", "strong", "sub", "summary", "sup", "textarea", "time", "u", "var", "wbr", "webview"; optional):
    The component used for the `input` element. Either a string to use
    a HTML element or a component.

- inputMode (a value equal to: "text", "none", "search", "tel", "url", "email", "numeric", "decimal"; optional):
    Hints at the type of data that might be entered by the user while
    editing the element or its contents.

- inputProps (boolean | number | string | dict | list; optional):
    [Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#Attributes)
    applied to the `input` element.

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

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- name (string; optional):
    Name attribute of the `input` element.

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

- value (boolean | number | string | dict | list; optional):
    The value of the `input` element, required for a controlled
    component.

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Input'
    @_explicitize_args
    def __init__(self, classes=Component.UNDEFINED, disableUnderline=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, ref=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, role=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, color=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, margin=Component.UNDEFINED, disabled=Component.UNDEFINED, type=Component.UNDEFINED, error=Component.UNDEFINED, name=Component.UNDEFINED, autoFocus=Component.UNDEFINED, value=Component.UNDEFINED, autoComplete=Component.UNDEFINED, readOnly=Component.UNDEFINED, required=Component.UNDEFINED, size=Component.UNDEFINED, rows=Component.UNDEFINED, fullWidth=Component.UNDEFINED, endAdornment=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, inputProps=Component.UNDEFINED, inputRef=Component.UNDEFINED, inputComponent=Component.UNDEFINED, multiline=Component.UNDEFINED, maxRows=Component.UNDEFINED, minRows=Component.UNDEFINED, startAdornment=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'about', 'accessKey', 'autoCapitalize', 'autoComplete', 'autoCorrect', 'autoFocus', 'autoSave', 'className', 'classes', 'color', 'components', 'componentsProps', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disableUnderline', 'disabled', 'draggable', 'endAdornment', 'error', 'fullWidth', 'hidden', 'inlist', 'inputComponent', 'inputMode', 'inputProps', 'inputRef', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'margin', 'maxRows', 'minRows', 'multiline', 'n_clicks', 'name', 'placeholder', 'prefix', 'property', 'radioGroup', 'readOnly', 'ref', 'required', 'resource', 'results', 'role', 'rows', 'security', 'size', 'slot', 'spellCheck', 'startAdornment', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'type', 'typeof', 'unselectable', 'value', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'about', 'accessKey', 'autoCapitalize', 'autoComplete', 'autoCorrect', 'autoFocus', 'autoSave', 'className', 'classes', 'color', 'components', 'componentsProps', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'disableUnderline', 'disabled', 'draggable', 'endAdornment', 'error', 'fullWidth', 'hidden', 'inlist', 'inputComponent', 'inputMode', 'inputProps', 'inputRef', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'lang', 'margin', 'maxRows', 'minRows', 'multiline', 'n_clicks', 'name', 'placeholder', 'prefix', 'property', 'radioGroup', 'readOnly', 'ref', 'required', 'resource', 'results', 'role', 'rows', 'security', 'size', 'slot', 'spellCheck', 'startAdornment', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'type', 'typeof', 'unselectable', 'value', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Input, self).__init__(**args)
