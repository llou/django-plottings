"""
    ========
    views.py
    ========

    This module provides with a collection of Django View classes that respond
    to requests with HttpResponse objects with Matplotlib figures as payload.

"""
from typing import Any
from django.views import View
from django.http import HttpResponse
from .base import CachedMixin, SVGZPlotMixin, PNGPlotMixin


class BasePlotView(View):
    """
    A Django View class that has the common logic of all project's View
    classes. It is not intended to be used in production but instead to be
    subclassed and extended via mixins.
    """
    http_response_class = HttpResponse
    buffer_class: Any = None
    file_format = ""
    filename = ""
    encoding = ""
    disposition = ""  # values: inline, attachment
    mimetype = ""
    http_method_names = [
            "get",
            "head",
            "options",
    ]

    def get_disposition(self):
        """
        Override this method if you want to dinamically set the content
        disposition of the ``HttpResponse`` object.
        """
        return self.disposition

    def get_filename(self):
        """
        Override this method if you want to dinamically set the name of
        the file generated from the figure when the disposition is attachment.
        """
        return self.filename

    def get_mimetype(self):
        """
        Override this method if you want to dinamically set the mimetype of
        the generated file.
        """
        return self.mimetype

    def get_encoding(self):
        """
        Override this method if you want to dinamically set the encoding of
        the generated file.
        """
        return self.encoding

    def get_headers(self, buffer):
        """
        Returns a dict of parameters to be used as headers of the response
        object. Override it to provide extend the values it contains.
        """
        result = {}

        disposition = self.get_disposition()
        if disposition:
            if disposition == "inline":
                result['Content-Disposition'] = 'inline'
            else:
                name = self.get_filename()
                value = f'attachment; filename="{name}"'
                result['Content-Disposition'] = value

        encoding = self.get_encoding()
        if encoding:
            result['Content-Encoding'] = encoding
        result['Content-Length'] = buffer.getbuffer().nbytes
        return result

    def get(self, request, *args, **kwargs):
        """
        This methods generates the GET response.
        """
        buffer = self.get_image()
        headers = self.get_headers(buffer)

        response = self.http_response_class(buffer,
                                            content_type=self.get_mimetype())
        for key, value in headers.items():
            response.headers[key] = value
        return response

    def head(self, request, *args, **kwargs):
        """
        This methods generates the HEAD response.
        """
        buffer = self.get_image()
        headers = self.get_headers(buffer)

        response = self.http_response_class(b"",
                                            content_type=self.get_mimetype())
        for key, value in headers.items():
            response.headers[key] = value
        return response


class PNGPlotView(PNGPlotMixin, BasePlotView):
    """
    A Django ``View`` class that returns a PNG graphic file as ``HttpResponse``
    payload.
    """
    disposition = "inline"
    mimetype = "image/png"


class SVGZPlotView(SVGZPlotMixin, BasePlotView):
    """
    A Django `View` class that returns a SVGZ graphic file as `HttpResponse`
    payload.
    """
    disposition = "inline"
    encoding = "gzip"
    mimetype = "image/svg+xml"


class CachedPNGPlotView(CachedMixin, PNGPlotMixin, BasePlotView):
    """
    A Django ``View`` class that returns a PNG graphic file as ``HttpResponse``
    payload.
    """
    disposition = "inline"
    mimetype = "image/png"


class CachedSVGZPlotView(CachedMixin, SVGZPlotMixin, BasePlotView):
    """
    A Django `View` class that returns a SVGZ graphic file as `HttpResponse`
    payload.
    """
    disposition = "inline"
    encoding = "gzip"
    mimetype = "image/svg+xml"


SVGViewPlot = CachedSVGZPlotView
PNGViewPlot = CachedPNGPlotView
