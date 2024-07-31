"""
A library to generate Matplotilib graphics within django applications
"""

from .views import (
        PNGPlotView,
        SVGZPlotView,
        CachedPNGPlotView,
        CachedSVGZPlotView,
        PNGView,
        SVGView,
        )
from .value import (
        SVGPlotToValue,
        PNGBase64PlotToValue,
        CachedSVGPlotToValue,
        CachedPNGBase64PlotToValue,
        SVGValue,
        PNGValue,
        )
from .file import (
        SVGZPlotToFile,
        PNGPlotToFile,
        CachedSVGZPlotToFile,
        CachedPNGPlotToFile,
        SVGFile,
        PNGFile,
        )

__all__ = ["PNGPlotView",
           "SVGZPlotView",
           "PNGPlotToFile",
           "SVGZPlotToFile",
           "SVGPlotToValue",
           "PNGBase64PlotToValue"
           "CachedPNGPlotView",
           "CachedSVGZPlotView",
           "CachedPNGPlotToFile",
           "CachedSVGZPlotToFile",
           "CachedSVGPlotToValue",
           "PNGBase64PlotToValue"
           "PNGView",
           "SVGView",
           "PNGFile",
           "SVGFile",
           "PNGValue",
           "SVGValue",
           ]

__version__ = "0.0.1"
