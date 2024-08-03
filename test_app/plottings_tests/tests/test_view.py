from io import BytesIO
from django.test import TestCase, Client
from django.test.client import RequestFactory
from plottings.views import BasePlotView, PNGPlotView, SVGZPlotView


# os.environ['DJANGO_SETTINGS_MODULE'] = "test_app.settings"

class TestBlackBox(TestCase):
    def test_server(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_png_get(self):
        client = Client()
        response = client.get("/activity.png")
        content = response.content
        self.assertValidPNG(content)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Content-Length", response.headers)
        self.assertNotEqual(response.headers["Content-Length"], 0)

    def test_png_head(self):
        client = Client()
        response = client.head("/activity.png")
        content = response.content
        self.assertEqual(content, b"")

    def test_svgz_get(self):
        client = Client()
        response = client.get("/activity.svgz")
        content = response.content
        self.assertValidSVG(content)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Content-Length", response.headers)
        self.assertNotEqual(response.headers["Content-Length"], 0)

    def test_svgz_head(self):
        client = Client()
        response = client.head("/activity.svgz")
        content = response.content
        self.assertEqual(content, b"")

    def assertValidSVG(self, content):
        pass

    def assertValidPNG(self, content):
        pass


class TestViewMixin:
    tclass = BasePlotView
    buffer_class = BytesIO
    filename = ""
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

            def get_mimetype(self2):
                return self.mimetype

            def get_image(self2):
                self.buffer = self.buffer_class()
                self.buffer.write(self.output)
                self.buffer.seek(0)
                return self.buffer

        self.view = MockView.as_view()

    def test_get(self):
        request = RequestFactory().get("/" + self.filename)
        response = self.view(request)
        content = response.content
        self.assertEqual(content, self.output)
        self.assertIn("Content-Length", response.headers)
        self.assertEqual(response.headers["Content-Length"],
                         str(len(self.output)))

    def test_head(self):
        request = RequestFactory().head("/" + self.filename)
        response = self.view(request)
        content = response.content
        self.assertEqual(content, b"")
        self.assertIn("Content-Length", response.headers)
        self.assertEqual(response.headers["Content-Length"],
                         str(len(self.output)))


class TextFileViewTestCase(TestViewMixin, TestCase):
    filename = "text.txt"
    file_format = "txt"


class PNGPlotViewTestCase(TestViewMixin, TestCase):
    tclass = PNGPlotView
    filename = "activity.png"
    mimetype = "image/x-png"
    file_format = "png"
    output = b"\x00\x00\x00"


class SVGPlotViewTestCase(TestViewMixin, TestCase):
    tclass = SVGZPlotView
    encoding = "gzip"
    filename = "activity.svgz"
    mimetype = "image/svg+xml"
    file_format = "svgz"
    output = b"\x00\x00\x00"
