from .base import BasePlotMixin, StorageMixin, SVGPlotMixin, PNGPlotMixin


class SVGPlotToFile(StorageMixin, SVGPlotMixin, BasePlotMixin):
    pass


class PNGPlotToFile(StorageMixin, PNGPlotMixin, BasePlotMixin):
    pass
