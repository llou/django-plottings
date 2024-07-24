from .base import (
        BasePlot,
        ValueMixin,
        SVGPlotMixin,
        PNGPlotMixin,
        Base64PlotMixin
)


class SVGPlotToValue(SVGPlotMixin, ValueMixin, BasePlot):
    pass


class PNGBase64PlotToValue(Base64PlotMixin, PNGPlotMixin, ValueMixin,
                           BasePlot):
    pass
