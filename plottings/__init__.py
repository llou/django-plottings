"""
A library to generate Matplotilib graphics within django applications
"""

from .views import PNGPlotView, SVGZPlotView
from .value import SVGPlotToValue, PNGBase64PlotToValue
from .file import SVGZPlotToFile, PNGPlotToFile

__all__ = ["PNGPlotView",
           "SVGZPlotView",
           "PNGPlotToFile",
           "SVGZPlotToFile",
           "SVGPlotToValue",
           "PNGBase64PlotToValue"
           ]

__version__ = "0.0.1"
