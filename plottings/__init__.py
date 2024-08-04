"""
A library to generate Matplotilib graphics within django applications
"""

from .views import (
        PNGPlotView,
        SVGZPlotView,
        CachedPNGPlotView,
        CachedSVGZPlotView,
        PNGViewPlot,
        SVGViewPlot,
        )
from .value import (
        SVGPlotToValue,
        PNGBase64PlotToValue,
        CachedSVGPlotToValue,
        CachedPNGBase64PlotToValue,
        SVGValuePlot,
        PNGValuePlot,
        )
from .file import (
        SVGZPlotToFile,
        PNGPlotToFile,
        SVGFilePlot,
        PNGFilePlot,
        )

__all__ = ["PNGPlotView",
           "SVGZPlotView",
           "PNGPlotToFile",
           "SVGZPlotToFile",
           "SVGPlotToValue",
           "PNGBase64PlotToValue"
           "CachedPNGPlotView",
           "CachedSVGZPlotView",
           "CachedSVGPlotToValue",
           "PNGBase64PlotToValue"
           "PNGViewPlot",
           "SVGViewPlot",
           "PNGFilePlot",
           "SVGFilePlot",
           "PNGValuePlot",
           "SVGValuePlot",
           ]

__version__ = "0.0.3"
