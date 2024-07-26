"""
    =======
    file.py
    =======

    This module provides the classes required to generate django files ready to
    be stored in media directories.
"""
from .base import BasePlot, FileMixin, SVGZPlotMixin, PNGPlotMixin


class SVGZPlotToFile(SVGZPlotMixin, FileMixin, BasePlot):
    """
    This class is used to create a django a file object storing a SVG plot
    of the plotter function
    """
    pass


class PNGPlotToFile(PNGPlotMixin, FileMixin, BasePlot):
    """
    This class is used to create a django a file object storing a PNG plot
    of the plotter function
    """
    pass
