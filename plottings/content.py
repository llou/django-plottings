from .base import (
        BasePlot,
        ContentMixin,
        SVGPlotMixin,
        PNGPlotMixin,
        Base64PlotMixin,
        )


class SVGPlotToVar(SVGPlotMixin, ContentMixin, BasePlot):
    pass


class PNGBase64PlotToVar(Base64PlotMixin, PNGPlotMixin, ContentMixin,
                         BasePlot):
    pass
