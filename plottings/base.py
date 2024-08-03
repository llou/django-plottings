"""
    =======
    base.py
    =======

    This module contains the basic classes used for building the actual classes
    that are used in generating the plots. It is structured around a base class
    called ``BasePlot`` that implements the common logic required for the
    project operations with some mixin_ classes to add it extra functionality
    by multiple inheritance.

    .. _mixin: https://en.wikipedia.org/wiki/Mixin
"""

from typing import Any
from io import BytesIO, StringIO
from contextlib import contextmanager
import matplotlib.pyplot as plt
from django.core.cache import caches


class BasePlot:
    """
    Base class of all the plot classes used in this library. It implements the
    basic protocol that gathers the data, draws the graph and passes it to an
    in memory file like object ready to be consumed.
    """
    buffer_class: Any = BytesIO
    file_format = ""

    @staticmethod
    def plotter_function(data, **kwargs):
        """
        Override this method with an **statically linked function** that
        returns a Matplotlib figure to be lately used to render the plot
        in given file formats.

        :data: A data structure that contains the information to be graphically
            modeled by the plotter function.

        :kwargs: A dict of parameters used to customize the image rendering.

        """
        raise NotImplementedError("Plot class requires a plotter method")

    def get_plot_data(self):
        """
        Override this method to provide data to ``plotter_function()``
        method.
        """
        return {}

    def get_plot_options(self):
        """
        Override this method to provide the plotter function with extra
        parameters to customize the graphical generation.
        """
        return {}

    def get_filetype(self):
        """
        Override this method to dinamically set the file format of the
        generated file.
        """
        return self.file_format

    @contextmanager
    def _get_figure(self):
        data = self.get_plot_data()
        plot_options = self.get_plot_options()
        figure = self.plotter_function(data, **plot_options)
        try:
            yield figure
        finally:
            plt.close(figure)

    def process_image(self, image_buffer):
        """
        Override this method to add modifications to the image such as
        watermarks before caching.
        """
        return image_buffer

    def get_image(self):
        """
        Returns a in memory file object with the plot image.
        """
        image_buffer = self.buffer_class()
        with self._get_figure() as figure:
            figure.savefig(image_buffer, format=self.get_filetype())
        image_buffer = self.process_image(image_buffer)
        image_buffer.seek(0)
        return image_buffer


class CachedMixin:
    """
    Mixin class to add cache functionality to the BasePlot object.
    """
    cache_backend_name = "default"
    cache_timeout = -1

    def get_cache_key(self):
        """
        Override this method with a value that changes when plot regeneration
        is required.
        """
        raise NotImplementedError

    def get_image(self):
        cache_backend = caches[self.cache_backend_name]
        cache_key = self.get_cache_key()
        image_value = cache_backend.get(cache_key)

        if image_value is None:
            image_file = super().get_image()
            image_value = image_file.getvalue()
            if self.cache_timeout == -1:
                cache_backend.set(cache_key, image_value)
            else:
                cache_backend.set(cache_key, image_value, self.cache_timeout)
            return image_file
        else:
            return self.buffer_class(image_value)


class SVGPlotMixin(BasePlot):
    """
    Mixing to generate a memory file containing an SVG figure.
    """
    buffer_class = StringIO
    file_format = "svg"


class SVGZPlotMixin(BasePlot):
    """
    Mixin to generate a memory file containing an SVGZ figure.
    """
    buffer_class = BytesIO
    file_format = "svgz"


class PNGPlotMixin(BasePlot):
    """
    Mixin to generate a memory file containing a binary PNG figure.
    """
    buffer_class = BytesIO
    file_format = "png"
