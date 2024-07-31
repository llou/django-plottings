"""
    =======
    base.py
    =======

    This module contains most of the basic classes used in generating the
    plots and dumping them into file object or variables to be lately used
    in Django.
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

    def get_plot_kwargs(self):
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
        plot_kwargs = self.get_plot_kwargs()
        figure = self.plotter_function(data, **plot_kwargs)
        try:
            yield figure
        finally:
            plt.close(figure)

    def process_image(self, image):
        """
        Override this method to add modifications to the image such as
        watermarks before caching.
        """
        return image

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
