# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CardHeader(Component):
    """A CardHeader component.
Material-UI CardHeader.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- action (boolean | number | string | dict | list; optional):
    The action to display in the card header.

- avatar (boolean | number | string | dict | list; optional):
    The Avatar element to display.

- className (string; optional)

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- disableTypography (boolean; optional):
    If `True`, `subheader` and `title` won't be wrapped by a
    Typography component. This can be useful to render an alternative
    Typography variant by wrapping the `title` text, and optional
    `subheader` text with the Typography component.

- style (boolean | number | string | dict | list; optional)

- subheader (boolean | number | string | dict | list; optional):
    The content of the component.

- subheaderTypographyProps (boolean | number | string | dict | list; optional):
    These props will be forwarded to the subheader (as long as
    disableTypography is not `True`).

- sx (dict; optional):
    The system prop that allows defining system overrides as well as
    additional CSS styles.

- title (boolean | number | string | dict | list; optional):
    The content of the component.

- titleTypographyProps (boolean | number | string | dict | list; optional):
    These props will be forwarded to the title (as long as
    disableTypography is not `True`)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'CardHeader'
    @_explicitize_args
    def __init__(self, component=Component.UNDEFINED, action=Component.UNDEFINED, avatar=Component.UNDEFINED, classes=Component.UNDEFINED, disableTypography=Component.UNDEFINED, subheader=Component.UNDEFINED, subheaderTypographyProps=Component.UNDEFINED, sx=Component.UNDEFINED, title=Component.UNDEFINED, titleTypographyProps=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'action', 'avatar', 'className', 'classes', 'component', 'disableTypography', 'style', 'subheader', 'subheaderTypographyProps', 'sx', 'title', 'titleTypographyProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'action', 'avatar', 'className', 'classes', 'component', 'disableTypography', 'style', 'subheader', 'subheaderTypographyProps', 'sx', 'title', 'titleTypographyProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(CardHeader, self).__init__(**args)
