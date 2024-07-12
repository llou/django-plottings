"""
A library to generate Matplotilib graphics within django applications
"""

from .file import SVGPlotToFile, PNGPlotToFile
from .views import PNGPlotView, SVGPlotView
from .memory import SVGPlot, PNGBase64Plot

__all__ = ["SVGPlotToFile",
           "PNGPlotToFile",
           "PNGPlotView",
           "SVGPlotView",
           "SVGPlot",
           "PNGBase64Plot"
           ]

__version__ = "0.0.1"
