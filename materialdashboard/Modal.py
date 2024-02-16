# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Modal(Component):
    """A Modal component.
Material-UI Modal.

Keyword arguments:

- children (boolean | number | string | dict | list; optional):
    A single child content element.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- BackdropComponent (a value equal to: "symbol" | a value equal to: "object" | a value equal to: "style" | a value equal to: "div" | a value equal to: "a" | a value equal to: "abbr" | a value equal to: "address" | a value equal to: "area" | a value equal to: "article" | a value equal to: "aside" | a value equal to: "audio" | a value equal to: "b" | a value equal to: "base" | a value equal to: "bdi" | a value equal to: "bdo" | a value equal to: "big" | a value equal to: "blockquote" | a value equal to: "body" | a value equal to: "br" | a value equal to: "button" | a value equal to: "canvas" | a value equal to: "caption" | a value equal to: "cite" | a value equal to: "code" | a value equal to: "col" | a value equal to: "colgroup" | a value equal to: "data" | a value equal to: "datalist" | a value equal to: "dd" | a value equal to: "del" | a value equal to: "details" | a value equal to: "dfn" | a value equal to: "dialog" | a value equal to: "dl" | a value equal to: "dt" | a value equal to: "em" | a value equal to: "embed" | a value equal to: "fieldset" | a value equal to: "figcaption" | a value equal to: "figure" | a value equal to: "footer" | a value equal to: "form" | a value equal to: "h1" | a value equal to: "h2" | a value equal to: "h3" | a value equal to: "h4" | a value equal to: "h5" | a value equal to: "h6" | a value equal to: "head" | a value equal to: "header" | a value equal to: "hgroup" | a value equal to: "hr" | a value equal to: "html" | a value equal to: "i" | a value equal to: "iframe" | a value equal to: "img" | a value equal to: "input" | a value equal to: "ins" | a value equal to: "kbd" | a value equal to: "keygen" | a value equal to: "label" | a value equal to: "legend" | a value equal to: "li" | a value equal to: "link" | a value equal to: "main" | a value equal to: "map" | a value equal to: "mark" | a value equal to: "menu" | a value equal to: "menuitem" | a value equal to: "meta" | a value equal to: "meter" | a value equal to: "nav" | a value equal to: "noindex" | a value equal to: "noscript" | a value equal to: "ol" | a value equal to: "optgroup" | a value equal to: "option" | a value equal to: "output" | a value equal to: "p" | a value equal to: "param" | a value equal to: "picture" | a value equal to: "pre" | a value equal to: "progress" | a value equal to: "q" | a value equal to: "rp" | a value equal to: "rt" | a value equal to: "ruby" | a value equal to: "s" | a value equal to: "samp" | a value equal to: "slot" | a value equal to: "script" | a value equal to: "section" | a value equal to: "select" | a value equal to: "small" | a value equal to: "source" | a value equal to: "span" | a value equal to: "strong" | a value equal to: "sub" | a value equal to: "summary" | a value equal to: "sup" | a value equal to: "table" | a value equal to: "template" | a value equal to: "tbody" | a value equal to: "td" | a value equal to: "textarea" | a value equal to: "tfoot" | a value equal to: "th" | a value equal to: "thead" | a value equal to: "time" | a value equal to: "title" | a value equal to: "tr" | a value equal to: "track" | a value equal to: "u" | a value equal to: "ul" | a value equal to: "var" | a value equal to: "video" | a value equal to: "wbr" | a value equal to: "webview" | a value equal to: "svg" | a value equal to: "animate" | a value equal to: "animateMotion" | a value equal to: "animateTransform" | a value equal to: "circle" | a value equal to: "clipPath" | a value equal to: "defs" | a value equal to: "desc" | a value equal to: "ellipse" | a value equal to: "feBlend" | a value equal to: "feColorMatrix" | a value equal to: "feComponentTransfer" | a value equal to: "feComposite" | a value equal to: "feConvolveMatrix" | a value equal to: "feDiffuseLighting" | a value equal to: "feDisplacementMap" | a value equal to: "feDistantLight" | a value equal to: "feDropShadow" | a value equal to: "feFlood" | a value equal to: "feFuncA" | a value equal to: "feFuncB" | a value equal to: "feFuncG" | a value equal to: "feFuncR" | a value equal to: "feGaussianBlur" | a value equal to: "feImage" | a value equal to: "feMerge" | a value equal to: "feMergeNode" | a value equal to: "feMorphology" | a value equal to: "feOffset" | a value equal to: "fePointLight" | a value equal to: "feSpecularLighting" | a value equal to: "feSpotLight" | a value equal to: "feTile" | a value equal to: "feTurbulence" | a value equal to: "filter" | a value equal to: "foreignObject" | a value equal to: "g" | a value equal to: "image" | a value equal to: "line" | a value equal to: "linearGradient" | a value equal to: "marker" | a value equal to: "mask" | a value equal to: "metadata" | a value equal to: "mpath" | a value equal to: "path" | a value equal to: "pattern" | a value equal to: "polygon" | a value equal to: "polyline" | a value equal to: "radialGradient" | a value equal to: "rect" | a value equal to: "stop" | a value equal to: "switch" | a value equal to: "text" | a value equal to: "textPath" | a value equal to: "tspan" | a value equal to: "use" | a value equal to: "view" | boolean | number | string | dict | list; optional):
    A backdrop component. This prop enables custom backdrop rendering.

- BackdropProps (boolean | number | string | dict | list; optional):
    Props applied to the [`Backdrop`](/api/backdrop/) element.   Props
    applied to the [`BackdropUnstyled`](/api/backdrop-unstyled/)
    element.

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- closeAfterTransition (boolean; optional):
    When set to True the Modal waits until a nested Transition is
    completed before closing.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

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

- hideBackdrop (boolean; optional):
    If `True`, the backdrop is not rendered.

- keepMounted (boolean; optional):
    Always keep the children in the DOM. This prop can be useful in
    SEO situation or when you want to maximize the responsiveness of
    the Modal.

- open (boolean; optional):
    If `True`, the component is shown.

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Modal'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, BackdropComponent=Component.UNDEFINED, BackdropProps=Component.UNDEFINED, sx=Component.UNDEFINED, classes=Component.UNDEFINED, closeAfterTransition=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, container=Component.UNDEFINED, disableAutoFocus=Component.UNDEFINED, disableEnforceFocus=Component.UNDEFINED, disableEscapeKeyDown=Component.UNDEFINED, disablePortal=Component.UNDEFINED, disableRestoreFocus=Component.UNDEFINED, disableScrollLock=Component.UNDEFINED, hideBackdrop=Component.UNDEFINED, keepMounted=Component.UNDEFINED, open=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'BackdropComponent', 'BackdropProps', 'classes', 'closeAfterTransition', 'component', 'components', 'componentsProps', 'container', 'disableAutoFocus', 'disableEnforceFocus', 'disableEscapeKeyDown', 'disablePortal', 'disableRestoreFocus', 'disableScrollLock', 'hideBackdrop', 'keepMounted', 'open', 'sx']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'BackdropComponent', 'BackdropProps', 'classes', 'closeAfterTransition', 'component', 'components', 'componentsProps', 'container', 'disableAutoFocus', 'disableEnforceFocus', 'disableEscapeKeyDown', 'disablePortal', 'disableRestoreFocus', 'disableScrollLock', 'hideBackdrop', 'keepMounted', 'open', 'sx']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Modal, self).__init__(children=children, **args)
