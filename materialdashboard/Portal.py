# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Portal(Component):
    """A Portal component.
Material-UI Portal.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children to render into the `container`.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- container (string; optional):
    An HTML element or function that returns one. The `container` will
    have the portal children appended to it.  By default, it uses the
    body of the top-level document object, so it's simply
    `document.body` most of the time. If specified, the ID of an
    existing element should be provided.

- disablePortal (boolean; optional):
    The `children` will be under the DOM hierarchy of the parent
    component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'Portal'
    @_explicitize_args
    def __init__(self, children=None, container=Component.UNDEFINED, disablePortal=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'container', 'disablePortal']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'container', 'disablePortal']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Portal, self).__init__(children=children, **args)
