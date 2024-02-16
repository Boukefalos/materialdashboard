# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SliderValueLabelUnstyled(Component):
    """A SliderValueLabelUnstyled component.
Material-UI SliderValueLabelUnstyled.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- className (string; optional)

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the ValueLabel. Either a
    string to use a HTML element or a component.

- style (boolean | number | string | dict | list; optional)

- value (number | list of numbers; optional):
    The value of the slider. For ranged sliders, provide an array with
    two values.

- valueLabelDisplay (a value equal to: "on", "off", "auto"; optional):
    Controls when the value label is displayed:  - `auto` the value
    label will display when the thumb is hovered or focused. - `on`
    will display persistently. - `off` will never display."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'SliderValueLabelUnstyled'
    @_explicitize_args
    def __init__(self, className=Component.UNDEFINED, style=Component.UNDEFINED, components=Component.UNDEFINED, value=Component.UNDEFINED, valueLabelDisplay=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'components', 'style', 'value', 'valueLabelDisplay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'components', 'style', 'value', 'valueLabelDisplay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(SliderValueLabelUnstyled, self).__init__(**args)
