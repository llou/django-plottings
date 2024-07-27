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
from base64 import b64encode
from django.core.files import File as DjangoFile
from django.utils.safestring import mark_safe


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

    def get_cache_key(self):
        """
        Override this method with a value that changes when plot regeneration
        is required.
        """
        return 0

    def _get_figure(self):
        data = self.get_plot_data()
        plot_kwargs = self.get_plot_kwargs()
        return self.plotter_function(data, **plot_kwargs)

    def _get_buffer(self):
        buffer = self.buffer_class()
        figure = self._get_figure()
        figure.savefig(buffer, format=self.get_filetype())
        buffer.seek(0)
        return buffer


class ValueMixin:
    """
    This mixins provides ``BasePlot`` with the ``get_value()`` method that
    returns a safe string to be used inside a template.
    """

    def get_value(self):
        """
        Add the returned value of this method to the context dictionary that is
        passed to render the template.
        """
        buffer = self._get_buffer()
        value = buffer.getvalue()
        return mark_safe(value)


class Base64ValueMixin:
    """
    This mixin provides the ``BasePlot`` class with base64 encoding of its
    provided value through ``get_value()`` method.
    """
    def get_value(self):
        """
        Add the returned value of this method to the context dictionary that is
        passed to render the template.
        """
        buffer = self._get_buffer()
        value = buffer.getvalue()
        return mark_safe(b64encode(value).decode("utf-8"))


class FileMixin:
    """
    This mixin provides the ``BasePlot`` class with the capability of
    generating a in memory file to be passed to an Image field.
    """
    file_class = DjangoFile
    filename = ""

    def get_filename(self):
        """
        Override this method to dinamically change the name of the file object
        created by the ``get_file()`` method.
        """
        name = self.filename
        ext = self.get_filetype()
        return f"{name}.{ext}"

    def get_file(self):
        """
        This method returns a Django file object ready to be assigned to an
        ImageField.
        """
        name = self.get_filename()
        file = self.file_class(self._get_buffer(), name)
        return file


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
