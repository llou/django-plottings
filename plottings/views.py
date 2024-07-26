from io import BytesIO
from typing import Any
from django.views import View
from django.http import HttpResponse
from .base import BasePlot, SVGZPlotMixin, PNGPlotMixin

# TODO Add cache Headers


class BaseFileView(View):
    buffer_class: Any = None
    file_format = ""
    filename = ""
    encoding = ""
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

    def get_encoding(self):
        return self.encoding

    def get_headers(self):
        result = {}

        disposition = self.get_disposition()
        if disposition:
            if disposition == "inline":
                result['Content-Disposition'] = 'inline'
            else:
                name = self.get_filename()
                value = f'attrachment; filename="{name}"'
                result['Content-Disposition'] = value

        encoding = self.get_encoding()
        if encoding:
            result['Content-Encoding'] = encoding
        return result

    def _get_buffer(self):
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        buffer = self._get_buffer()
        response = HttpResponse(buffer, content_type=self.get_mimetype())
        headers = self.get_headers()
        for key, value in headers.items():
            response.headers[key] = value
        return response


class ImageView(BasePlot, BaseFileView):
    disposition = "inline"


class PNGPlotView(PNGPlotMixin, ImageView):
    def get_mimetype(self):
        return "image/png"


class SVGZPlotView(SVGZPlotMixin, ImageView):
    encoding = "gzip"

    def get_mimetype(self):
        return "image/svg+xml"
