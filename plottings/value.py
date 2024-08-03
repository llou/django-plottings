"""
    ========
    value.py
    ========

    This module provides with classes that assist in storing plots into
    variables ready to be passed to Django templates and include the plot
    within the html document.
"""
from base64 import b64encode
from django.utils.safestring import mark_safe
from .base import (
        BasePlot,
        CachedMixin,
        SVGPlotMixin,
        PNGPlotMixin,
)


class ValueMixin:
    """
    This mixins provides ``BasePlot`` with the ``get_value()`` method that
    returns a safe string to be used inside a template. It also has the magic
    method ``__str__.py`` so it can be inyected to the template.
    """

    def get_value(self):
        """
        Add the returned value of this method to the context dictionary that is
        passed to render the template.
        """
        image_buffer = self.get_image()
        value = image_buffer.getvalue()
        return mark_safe(value)

    def __str__(self):
        return self.get_value()


class Base64ValueMixin:
    """
    This mixin provides the ``BasePlot`` class with base64 encoding of its
    provided value through ``get_value()`` method. It also has the magic
    method ``__str__.py`` so it can be inyected to the template.

    """
    def get_value(self):
        """
        Add the returned value of this method to the context dictionary that is
        passed to render the template.
        """
        image_buffer = self.get_image()
        value = image_buffer.getvalue()
        return mark_safe(b64encode(value).decode("utf-8"))


class SVGPlotToValue(SVGPlotMixin, ValueMixin, BasePlot):
    """
    This class is used to create a SVG figure into a variable ready to
    be passed to the template engine to render it in a webpage.
    """
    pass


class PNGBase64PlotToValue(Base64ValueMixin, PNGPlotMixin, ValueMixin,
                           BasePlot):
    """
    This class is used to dump a PNG figure encoded in Base64 format into a
    variable ready to be passed to the template engine to render it in a
    webpage.
    """
    pass


class CachedSVGPlotToValue(CachedMixin, SVGPlotMixin, ValueMixin, BasePlot):
    """
    This class is used to create a SVG figure into a variable ready to
    be passed to the template engine to render it in a webpage. Cached Version.
    """
    pass


class CachedPNGBase64PlotToValue(CachedMixin, Base64ValueMixin, PNGPlotMixin,
                                 ValueMixin, BasePlot):
    """
    This class is used to dump a PNG figure encoded in Base64 format into a
    variable ready to be passed to the template engine to render it in a
    webpage. Cached Version.
    """
    pass


SVGValuePlot = CachedSVGPlotToValue
PNGValuePlot = CachedPNGBase64PlotToValue
