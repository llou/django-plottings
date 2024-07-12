from io import BytesIO
from django.views import View
from django.http import HttpResponse
from ..base import BasePlotMixin, SVGPlotMixin, PNGPlotMixin


class BaseFileView(View):
    buffer_class = BytesIO
    file_format = ""
    filename = ""
    disposition = ""  # values: inline, attachment
    mimetype = ""
    http_method_names = [
            "get",
            "options",
    ]

    def get_disposition(self):
        return self.disposition

    def get_filename(self):
        return self.filename

    def get_extension(self):
        return self.file_format

    def get_filetype(self):
        return self.file_format

    def get_mimetype(self):
        return self.mimetype

    def get_headers(self):
        name = self.get_filename()
        disposition = self.get_disposition()
        if disposition:
            return {"Content-Disposition": f'{disposition}; filename="{name}"'}
        else:
            return {}

    def get_buffer(self):
        return self.buffer_class()

    def get(self, request, *args, **kwargs):
        buffer = self.get_buffer()
        response = HttpResponse(buffer, content_type=self.get_mimetype())
        headers = self.get_headers()
        for key, value in headers.items():
            response.headers[key] = value
        return response


class ImageView(BasePlotMixin, BaseFileView):
    diposition = "inline"

    def get_mimetype(self):
        return f"image/{self.get_filetype()}"


class PNGPlotView(PNGPlotMixin, ImageView):
    pass


class SVGPlotView(SVGPlotMixin, ImageView):
    pass
