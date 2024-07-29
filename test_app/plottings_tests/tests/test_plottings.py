from typing import Any
from base64 import b64decode
from unittest import TestCase
from unittest.mock import Mock, MagicMock
import matplotlib.pyplot as plt
from plottings.base import BasePlot
from plottings import (
        PNGPlotView,
        SVGZPlotView,
        SVGPlotToValue,
        PNGBase64PlotToValue,
        SVGZPlotToFile,
        PNGPlotToFile,
        )


PLOT_DATA = [1, 2, 3, 4]
PLOT_KWARGS = {"A": 1, "B": 2}
PLOT_BINARY = b"\x00\x00\x00"
PLOT_TEXT = "<svg></svg>"


# TEST figure

class BasePlotterMixin():
    tclass = BasePlot

    def setUp(self):
        super().setUp()
        self.plotter_function_mock = MagicMock()

        class MockPlot(self.tclass):
            def get_plot_data(self):
                return PLOT_DATA

            def get_plot_kwargs(self):
                return PLOT_KWARGS

            plotter_function = self.plotter_function_mock

        self.plot = MockPlot()

    def test_plotter_function(self):
        with self.plot._get_figure() as figure:
            self.assertEqual(figure, self.plotter_function_mock.return_value)
            self.plotter_function_mock.assert_called_with(PLOT_DATA,
                                                          **PLOT_KWARGS)
        fignums = plt.get_fignums()
        self.assertEqual(len(fignums), 0)


class BinaryPlotterMixin(BasePlotterMixin):
    pass


class TextPlotterMixin(BasePlotterMixin):
    pass


class SVGPlotToValuePlotterTestCase(TextPlotterMixin, TestCase):
    tclass = SVGPlotToValue


class SVGZPlotViewPlotterTestCase(BinaryPlotterMixin, TestCase):
    tclass = SVGZPlotView


class SVGZPlotToFilePlotterTestCase(BinaryPlotterMixin, TestCase):
    tclass = SVGZPlotToFile


class PNGPlotViewPlotterTestCase(BinaryPlotterMixin, TestCase):
    tclass = PNGPlotView


class PNGBase64PlotToValuePlotterTestCase(BinaryPlotterMixin, TestCase):
    tclass = PNGBase64PlotToValue


class PNGPlotToFilePlotterTestCase(BinaryPlotterMixin, TestCase):
    tclass = PNGPlotToFile


# TEST Buffer

class BaseBufferMixin:
    tclass = BasePlot
    output: Any = ""

    def setUp(self):
        super().setUp()

        def savefig(buffer, format=self.file_type):
            buffer.write(self.output)

        figure = Mock()
        figure.savefig = savefig
        self.plotter_function_mock = MagicMock()
        self.plotter_function_mock.return_value = figure

        class MockPlot(self.tclass):
            def get_filetype(self2):
                return self.file_type

            plotter_function = self.plotter_function_mock

        self.plot = MockPlot()

    def test_plotter_function(self):
        buffer = self.plot._get_buffer()
        value = buffer.getvalue()
        self.assertEqual(value, self.output)


class BinaryBufferMixin(BaseBufferMixin):
    output = PLOT_BINARY


class TextBufferMixin(BaseBufferMixin):
    output = PLOT_TEXT
    file_type = "SVG"


class SVGPlotToValueBufferTestCase(TextBufferMixin, TestCase):
    tclass = SVGPlotToValue
    file_type = "SVG"


class SVGZPlotViewBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = SVGZPlotView
    file_type = "SVGZ"


class PNGPlotViewBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = PNGPlotView
    file_type = "PNG"


class PNGBase64PlotToValueBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = PNGBase64PlotToValue
    file_type = "PNG"


class SVGZPlotToFileBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = SVGZPlotToFile
    output = PLOT_BINARY
    file_type = "SVGZ"


class PNGPlotToFileBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = PNGPlotToFile
    output = PLOT_BINARY
    file_type = "PNG"


# TEST Explotation


# Values


class BaseValueMixin:
    tclass = BasePlot
    output: Any = ""

    def setUp(self):
        super().setUp()

        class MockPlot(self.tclass):
            def _get_buffer(self2):
                self.buffer = self2.buffer_class()
                self.buffer.write(self.output)
                self.buffer.seek(0)
                return self.buffer

        self.plot = MockPlot()

    def get_value(self):
        return str(self.plot.get_value())

    def test_value(self):
        value = self.get_value()
        assert value, self.output


class PNGPlotToBase64ValueTestCase(BaseValueMixin, TestCase):
    tclass = PNGBase64PlotToValue
    output = PLOT_BINARY

    def get_value(self):
        value = super().get_value()
        return b64decode(value)


class SVGPlotToValueTestCase(BaseValueMixin, TestCase):
    tclass = SVGPlotToValue
    output = PLOT_TEXT


# Files

class BaseFileMixin:
    tclass = BasePlot
    filename = "filename"
    output: Any = ""

    def setUp(self):
        super().setUp()

        class MockPlot(self.tclass):
            def _get_filename(self2):
                return self.filename

            def _get_buffer(self2):
                self.buffer = self2.buffer_class()
                self.buffer.write(self.output)
                self.buffer.seek(0)
                return self.buffer

        self.plot = MockPlot()

    def test_file(self):
        f = self.plot.get_file()
        with f.open() as f:
            self.assertEqual(self.output, f.read())


class PNGPlotToFileTestCase(BaseFileMixin, TestCase):
    tclass = PNGPlotToFile
    filename = "filename.png"
    output = PLOT_BINARY


class SVGZPlotToFileTestCase(BaseFileMixin, TestCase):
    tclass = SVGZPlotToFile
    filename = "filename.svgz"
    output = PLOT_BINARY
