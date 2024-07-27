"""
    =======
    file.py
    =======

    This module provides the classes required to generate Django files ready to
    be stored in media directories.
"""

from .base import BasePlot, FileMixin, SVGZPlotMixin, PNGPlotMixin


class SVGZPlotToFile(SVGZPlotMixin, FileMixin, BasePlot):
    """
    This class is used to create a Django a ``File`` object storing an SVGZ
    plot.
    """
    pass


class PNGPlotToFile(PNGPlotMixin, FileMixin, BasePlot):
    """
    This class is used to create a Django a ``File`` object storing a PNG plot.
    """
    pass
