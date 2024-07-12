from io import BytesIO
from base64 import b64encode
from django.core.files.storage import storages
from .plots.utils import plotter_function


class BasePlotMixin:
    plotter_function = plotter_function
    buffer_class = BytesIO
    file_format = ""

    def get_filetype(self):
        return self.file_format

    def get_data(self):
        return {}

    def get_plot_kwargs(self):
        return {}

    def get_buffer(self):
        buffer = super().get_buffer()
        data = self.get_data()
        plot_kwargs = self.get_plot_kwargs()
        figure = self.plotter_function(data, **plot_kwargs)
        figure.savefig(buffer, format=self.get_filetype())
        buffer.seek(0)
        return buffer


class ContentMixin:
    def get_content(self):
        buffer = self.get_buffer()
        return buffer.getvalue()


class SVGPlotMixin(BasePlotMixin):
    file_format = "svg"


class PNGPlotMixin(BasePlotMixin):
    file_format = "png"


class Base64PlotMixin:
    def get_content(self):
        content = super().get_content()
        return b64encode(content)


class StorageMixin:
    storage_name = "default"

    def select_storage(self):
        return storages[self.storage_name]

    def save(self):
        storage = self.select_storage()
        buffer = self.get_buffer()
        name = self.get_filename()
        storage.save(name, buffer)
