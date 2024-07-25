from typing import Any
from io import BytesIO, StringIO
from base64 import b64encode
from django.core.files import File as DjangoFile
from django.utils.safestring import mark_safe


class ValueItem:
    def __init__(self, plot, value):
        self.plot = plot
        self.value = value

    @property
    def cache_key(self):
        return self.plot.get_cache_key()

    def get_value(self):
        return self.value

    def __len__(self):
        return len(self.value)

    def __eq__(self, other):
        return self.get_value() == str(other)

    def __str__(self):
        # TODO Decodes everytime it renders.
        return mark_safe(self.get_value())


class B64ValueItem(ValueItem):
    def get_value(self):
        return b64encode(self.value).decode("utf-8")


class BasePlot:
    buffer_class: Any = BytesIO
    file_format = ""

    @staticmethod
    def plotter_function(data, **kwargs):
        raise NotImplementedError("Plot class requires a plotter method")

    def get_filetype(self):
        return self.file_format

    def get_data(self):
        return {}

    def get_cache_key(self):
        return 0

    def get_plot_kwargs(self):
        return {}

    def get_figure(self):
        data = self.get_data()
        plot_kwargs = self.get_plot_kwargs()
        return self.plotter_function(data, **plot_kwargs)

    def get_buffer(self):
        buffer = self.buffer_class()
        figure = self.get_figure()
        figure.savefig(buffer, format=self.get_filetype())
        buffer.seek(0)
        return buffer


class ValueMixin:
    value_class = ValueItem

    def get_value(self):
        buffer = self.get_buffer()
        value = buffer.getvalue()
        return self.value_class(self, value)


class FileMixin:
    file_class = DjangoFile
    filename = ""

    def get_filename(self):
        name = self.filename
        ext = self.get_filetype()
        return f"{name}.{ext}"

    def get_file(self):
        name = self.get_filename()
        file = self.file_class(self.get_buffer(), name)
        return file


class SVGPlotMixin(BasePlot):
    buffer_class = StringIO
    file_format = "svg"


class SVGZPlotMixin(BasePlot):
    buffer_class = BytesIO
    file_format = "svgz"


class PNGPlotMixin(BasePlot):
    buffer_class = BytesIO
    file_format = "png"


class Base64PlotMixin:
    value_class = B64ValueItem
