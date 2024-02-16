# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ExtendSliderUnstyled(Component):
    """An ExtendSliderUnstyled component.
Material-UI ExtendSliderUnstyled.

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- classes (boolean | number | string | dict | list; optional):
    Override or extend the styles applied to the component.

- component (string; optional):
    The component used for the root node. Either a string to use a
    HTML element or a component.

- components (boolean | number | string | dict | list; optional):
    The components used for each slot inside the Slider. Either a
    string to use a HTML element or a component.

- componentsProps (boolean | number | string | dict | list; optional):
    The props used for each slot inside the Slider.

- defaultValue (number | list of numbers; optional):
    The default value. Use when the component is not controlled.

- disableSwap (boolean; optional):
    If `True`, the active thumb doesn't swap when moving pointer over
    a thumb while dragging another thumb.

- disabled (boolean; optional):
    If `True`, the component is disabled.

- isRtl (boolean; optional):
    Indicates whether the theme context has rtl direction. It is set
    automatically.

- marks (list of boolean | number | string | dict | lists | a value equal to: false, true; optional):
    Marks indicate predetermined values to which the user can move the
    slider. If `True` the marks are spaced according the value of the
    `step` prop. If an array, it should contain objects with `value`
    and an optional `label` keys.

- max (number; optional):
    The maximum allowed value of the slider. Should not be equal to
    min.

- min (number; optional):
    The minimum allowed value of the slider. Should not be equal to
    max.

- name (string; optional):
    Name attribute of the hidden `input` element.

- orientation (a value equal to: "horizontal", "vertical"; optional):
    The component orientation.

- step (number; optional):
    The granularity with which the slider can step through values. (A
    \"discrete\" slider.) The `min` prop serves as the origin for the
    valid values. We recommend (max - min) to be evenly divisible by
    the step.  When step is `None`, the thumb can only be slid onto
    marks provided with the `marks` prop.

- tabIndex (number; optional):
    Tab index attribute of the hidden `input` element.

- track (a value equal to: false, "normal", "inverted"; optional):
    The track presentation:  - `normal` the track will render a bar
    representing the slider value. - `inverted` the track will render
    a bar representing the remaining slider value. - `False` the track
    will render without a bar.

- value (number | list of numbers; optional):
    The value of the slider. For ranged sliders, provide an array with
    two values.

- valueLabelDisplay (a value equal to: "on", "off", "auto"; optional):
    Controls when the value label is displayed:  - `auto` the value
    label will display when the thumb is hovered or focused. - `on`
    will display persistently. - `off` will never display.

- valueLabelFormat (string; optional):
    The format function the value label's value.  When a function is
    provided, it should have the following signature:  - {number}
    value The value label's value to format - {number} index The value
    label's index to format."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'materialdashboard'
    _type = 'ExtendSliderUnstyled'
    @_explicitize_args
    def __init__(self, component=Component.UNDEFINED, classes=Component.UNDEFINED, components=Component.UNDEFINED, componentsProps=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, disableSwap=Component.UNDEFINED, isRtl=Component.UNDEFINED, marks=Component.UNDEFINED, max=Component.UNDEFINED, min=Component.UNDEFINED, name=Component.UNDEFINED, orientation=Component.UNDEFINED, step=Component.UNDEFINED, tabIndex=Component.UNDEFINED, track=Component.UNDEFINED, value=Component.UNDEFINED, valueLabelDisplay=Component.UNDEFINED, valueLabelFormat=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'classes', 'component', 'components', 'componentsProps', 'defaultValue', 'disableSwap', 'disabled', 'isRtl', 'marks', 'max', 'min', 'name', 'orientation', 'step', 'tabIndex', 'track', 'value', 'valueLabelDisplay', 'valueLabelFormat']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'classes', 'component', 'components', 'componentsProps', 'defaultValue', 'disableSwap', 'disabled', 'isRtl', 'marks', 'max', 'min', 'name', 'orientation', 'step', 'tabIndex', 'track', 'value', 'valueLabelDisplay', 'valueLabelFormat']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ExtendSliderUnstyled, self).__init__(**args)
