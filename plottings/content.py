from .base import (
        BasePlotMixin,
        ContentMixin,
        SVGPlotMixin,
        PNGPlotMixin,
        Base64PlotMixin,
        )


class SVGPlotToVar(SVGPlotMixin, ContentMixin, BasePlotMixin):
    pass


class PNGBase64PlotToVar(Base64PlotMixin, PNGPlotMixin, ContentMixin,
                         BasePlotMixin):
    pass
