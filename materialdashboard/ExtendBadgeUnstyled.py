# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ExtendBadgeUnstyled(Component):
    """An ExtendBadgeUnstyled component.
Material-UI ExtendBadgeUnstyled.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The badge will be added relative to this node.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- anchorOrigin (boolean | number | string | dict | list; optional):
    The anchor of the badge.

- badgeContent (boolean | number | string | dict | list; optional):
    The content rendered within the badge.

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the Badge. Either a
    string to use a HTML element or a component.

- componentsProps (boolean | number | string | dict | list; optional):
    The props used for each slot inside the Badge.

- invisible (boolean; optional):
    If `True`, the badge is invisible.

- max (number; optional):
    Max count to show.

- overlap (a value equal to: "circular", "rectangular"; optional):
    Wrapped shape the badge should overlap.

- showZero (boolean; optional):
    Controls whether the badge is hidden when `badgeContent` is zero.

- variant (string; optional):
    The variant to use."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ExtendBadgeUnstyled'
    @_explicitize_args
    def __init__(self, children=None, component=Component.UNDEFINED, anchorOrigin=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, overlap=Component.UNDEFINED, badgeContent=Component.UNDEFINED, classes=Component.UNDEFINED, invisible=Component.UNDEFINED, max=Component.UNDEFINED, showZero=Component.UNDEFINED, variant=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'anchorOrigin', 'badgeContent', 'classes', 'component', 'components', 'componentsProps', 'invisible', 'max', 'overlap', 'showZero', 'variant']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'anchorOrigin', 'badgeContent', 'classes', 'component', 'components', 'componentsProps', 'invisible', 'max', 'overlap', 'showZero', 'variant']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ExtendBadgeUnstyled, self).__init__(children=children, **args)
