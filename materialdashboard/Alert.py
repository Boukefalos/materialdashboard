# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Alert(Component):
    """An Alert component.
Material-UI Alert.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the component.

- id (string; optional)

- about (string; optional)

- accessKey (string; optional)

- action (boolean | number | string | dict | list; optional):
    The action to display. It renders after the message, at the end of
    the alert.

- autoCapitalize (string; optional)

- autoCorrect (string; optional)

- autoSave (string; optional)

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- closeText (string; optional):
    Override the default label for the *close popup* icon button.  For
    localization purposes, you can use the provided
    [translations](/guides/localization/).

- color (a value equal to: "success", "info", "warning", "error"; optional):
    The main color for the alert. Unless provided, the value is taken
    from the `severity` prop.

- contentEditable (a value equal to: false, true, "true", "false", "inherit"; optional)

- contextMenu (string; optional)

- dangerouslySetInnerHTML (boolean | number | string | dict | list; optional)

- datatype (string; optional)

- defaultChecked (boolean; optional)

- defaultValue (string | number | boolean | number | string | dict | list; optional)

- dir (string; optional)

- draggable (a value equal to: false, true, "true", "false"; optional)

- elevation (number; optional):
    Shadow depth, corresponds to `dp` in the spec. It accepts values
    between 0 and 24 inclusive.

- hidden (boolean; optional)

- icon (boolean | number | string | dict | list; optional):
    Override the icon displayed before the children. Unless provided,
    the icon is mapped to the value of the `severity` prop. Set to
    `False` to remove the `icon`.

- iconMapping (boolean | number | string | dict | list; optional):
    The component maps the `severity` prop to a range of different
    icons, for instance success to `<SuccessOutlined>`. If you wish to
    change this mapping, you can provide your own. Alternatively, you
    can use the `icon` prop to override the icon displayed.

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

- role (string; optional):
    The ARIA role attribute of the element.

- security (string; optional)

- severity (a value equal to: "success", "info", "warning", "error"; optional):
    The severity of the alert. This defines the color and icon used.

- slot (string; optional)

- spellCheck (a value equal to: false, true, "true", "false"; optional)

- square (boolean; optional):
    If `True`, rounded corners are disabled.

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

- variant (a value equal to: "outlined", "standard", "filled"; optional):
    The variant to use.

- vocab (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Alert'
    @_explicitize_args
    def __init__(self, children=None, action=Component.UNDEFINED, classes=Component.UNDEFINED, closeText=Component.UNDEFINED, color=Component.UNDEFINED, severity=Component.UNDEFINED, icon=Component.UNDEFINED, role=Component.UNDEFINED, iconMapping=Component.UNDEFINED, variant=Component.UNDEFINED, sx=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, elevation=Component.UNDEFINED, square=Component.UNDEFINED, ref=Component.UNDEFINED, slot=Component.UNDEFINED, title=Component.UNDEFINED, key=Component.UNDEFINED, defaultChecked=Component.UNDEFINED, defaultValue=Component.UNDEFINED, suppressContentEditableWarning=Component.UNDEFINED, suppressHydrationWarning=Component.UNDEFINED, accessKey=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, id=Component.UNDEFINED, lang=Component.UNDEFINED, placeholder=Component.UNDEFINED, spellCheck=Component.UNDEFINED, tabIndex=Component.UNDEFINED, translate=Component.UNDEFINED, radioGroup=Component.UNDEFINED, about=Component.UNDEFINED, datatype=Component.UNDEFINED, inlist=Component.UNDEFINED, prefix=Component.UNDEFINED, property=Component.UNDEFINED, resource=Component.UNDEFINED, typeof=Component.UNDEFINED, vocab=Component.UNDEFINED, autoCapitalize=Component.UNDEFINED, autoCorrect=Component.UNDEFINED, autoSave=Component.UNDEFINED, itemProp=Component.UNDEFINED, itemScope=Component.UNDEFINED, itemType=Component.UNDEFINED, itemID=Component.UNDEFINED, itemRef=Component.UNDEFINED, results=Component.UNDEFINED, security=Component.UNDEFINED, unselectable=Component.UNDEFINED, inputMode=Component.UNDEFINED, dangerouslySetInnerHTML=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'about', 'accessKey', 'action', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'closeText', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'draggable', 'elevation', 'hidden', 'icon', 'iconMapping', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'key', 'lang', 'n_clicks', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'severity', 'slot', 'spellCheck', 'square', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'variant', 'vocab']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'about', 'accessKey', 'action', 'autoCapitalize', 'autoCorrect', 'autoSave', 'className', 'classes', 'closeText', 'color', 'contentEditable', 'contextMenu', 'dangerouslySetInnerHTML', 'datatype', 'defaultChecked', 'defaultValue', 'dir', 'draggable', 'elevation', 'hidden', 'icon', 'iconMapping', 'inlist', 'inputMode', 'is', 'itemID', 'itemProp', 'itemRef', 'itemScope', 'itemType', 'key', 'lang', 'n_clicks', 'placeholder', 'prefix', 'property', 'radioGroup', 'ref', 'resource', 'results', 'role', 'security', 'severity', 'slot', 'spellCheck', 'square', 'style', 'suppressContentEditableWarning', 'suppressHydrationWarning', 'sx', 'tabIndex', 'title', 'translate', 'typeof', 'unselectable', 'variant', 'vocab']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Alert, self).__init__(children=children, **args)
