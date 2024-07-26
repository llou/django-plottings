from .base import (
        BasePlot,
        ValueMixin,
        SVGPlotMixin,
        PNGPlotMixin,
        Base64PlotMixin
)


class SVGPlotToValue(SVGPlotMixin, ValueMixin, BasePlot):
    """
    This class is used to create a SVG figure into a Value object ready to
    be passed to the template engine to render it in a webpage.
    """
    pass


class PNGBase64PlotToValue(Base64PlotMixin, PNGPlotMixin, ValueMixin,
                           BasePlot):
    """
    This class is used to dump a PNG figure encoded in Base64 format into a
    Value object ready to be passed to the template engine to render it in a
    webpage.
    """
    pass
