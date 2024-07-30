"""
A library to generate Matplotilib graphics within django applications
"""

from .views import PNGPlotView, SVGZPlotView, PNGView, SVGView
from .value import SVGPlotToValue, PNGBase64PlotToValue, SVGValue, PNGValue
from .file import SVGZPlotToFile, PNGPlotToFile, SVGFile, PNGFile

__all__ = ["PNGPlotView",
           "SVGZPlotView",
           "PNGPlotToFile",
           "SVGZPlotToFile",
           "SVGPlotToValue",
           "PNGBase64PlotToValue"
           "PNGView",
           "SVGView",
           "PNGFile",
           "PNGFile",
           "PNGValue",
           "PNGValue",
           ]

__version__ = "0.0.1"
