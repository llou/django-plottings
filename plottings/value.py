"""
    ========
    value.py
    ========

    This module provides with classes that assist in building value objects
    ready to be passed to a django template and render the plot within an
    html page.
"""
from .base import (
        BasePlot,
        ValueMixin,
        Base64ValueMixin,
        SVGPlotMixin,
        PNGPlotMixin,
)


class SVGPlotToValue(SVGPlotMixin, ValueMixin, BasePlot):
    """
    This class is used to create a SVG figure into a Value object ready to
    be passed to the template engine to render it in a webpage.
    """
    pass


class PNGBase64PlotToValue(Base64ValueMixin, PNGPlotMixin, ValueMixin,
                           BasePlot):
    """
    This class is used to dump a PNG figure encoded in Base64 format into a
    Value object ready to be passed to the template engine to render it in a
    webpage.
    """
    pass
