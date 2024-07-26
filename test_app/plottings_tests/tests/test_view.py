import os
from io import BytesIO
from django.test import TestCase
from django.test.client import RequestFactory
from plottings.views import BaseFileView, PNGPlotView, SVGZPlotView


os.environ['DJANGO_SETTINGS_MODULE'] = "plottings.tests.test_settings"


class TestViewMixin:
    tclass = BaseFileView
    buffer_class = BytesIO
    filename = ""
    filet_format = ""
    mimetype = "text/plain"
    disposition = "inline"
    output = b"texto"

    def setUp(self):
        super().setUp()

        class MockView(self.tclass):

            def get_disposition(self2):
                return self.disposition

            def get_filename(self2):
                return self.filename

            def get_extension(self2):
                return self.file_format

            def get_filetype(self2):
                return self.file_format

            def get_mimetype(self2):
                return self.mimetype

            def _get_buffer(self2):
                self.buffer = self.buffer_class()
                self.buffer.write(self.output)
                self.buffer.seek(0)
                return self.buffer

        self.view = MockView.as_view()

    def test_value(self):
        request = RequestFactory().get("/" + self.filename)
        response = self.view(request)
        content = response.content
        self.assertEqual(content, self.output)


class TextFileViewTestCase(TestViewMixin, TestCase):
    filename = "text.txt"
    file_format = "txt"


class PNGPlotViewTestCase(TestViewMixin, TestCase):
    tclass = PNGPlotView
    filename = "image.png"
    mimetype = "image/x-png"
    file_format = "png"
    output = b"\x00\x00\x00"


class SVGPlotViewTestCase(TestViewMixin, TestCase):
    tclass = SVGZPlotView
    encoding = "gzip"
    filename = "image.svgz"
    mimetype = "image/svg+xml"
    file_format = "svgz"
    output = b"\x00\x00\x00"
