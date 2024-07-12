from .base import (
        BasePlotMixin,
        ContentMixin,
        SVGPlotMixin,
        PNGPlotMixin,
        Base64PlotMixin
)


class SVGPlot(SVGPlotMixin, ContentMixin, BasePlotMixin):
    pass


class PNGBase64Plot(Base64PlotMixin, PNGPlotMixin, ContentMixin,
                    BasePlotMixin):
    pass
