"""
    ========
    value.py
    ========

    This module provides with classes that assist in storing plots into
    variables ready to be passed to Django templates and include the plot
    within the html document.
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
    This class is used to create a SVG figure into a variable ready to
    be passed to the template engine to render it in a webpage.
    """
    pass


class PNGBase64PlotToValue(Base64ValueMixin, PNGPlotMixin, ValueMixin,
                           BasePlot):
    """
    This class is used to dump a PNG figure encoded in Base64 format into a
    variable ready to be passed to the template engine to render it in a
    webpage.
    """
    pass
