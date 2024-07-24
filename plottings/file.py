from .base import BasePlot, FileMixin, SVGZPlotMixin, PNGPlotMixin


class SVGZPlotToFile(SVGZPlotMixin, FileMixin, BasePlot):
    pass


class PNGPlotToFile(PNGPlotMixin, FileMixin, BasePlot):
    pass
