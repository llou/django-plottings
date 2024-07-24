from typing import Any
from base64 import b64decode
from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from plottings.base import BasePlot
from plottings import (
        SVGPlotToFile,
        PNGPlotToFile,
        PNGPlotView,
        SVGZPlotView,
        SVGPlotToValue,
        PNGBase64PlotToValue,
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
            def get_data(self):
                return PLOT_DATA

            def get_plot_kwargs(self):
                return PLOT_KWARGS

            plotter_function = self.plotter_function_mock

        self.plot = MockPlot()

    def test_plotter_function(self):
        figure = self.plot.get_figure()
        self.assertEqual(figure, self.plotter_function_mock.return_value)
        self.plotter_function_mock.assert_called_with(PLOT_DATA,
                                                      **PLOT_KWARGS)


class BinaryPlotterMixin(BasePlotterMixin):
    pass


class TextPlotterMixin(BasePlotterMixin):
    pass


class SVGPlotToFilePlotterTestCase(TextPlotterMixin, TestCase):
    pass


class SVGPlotToValuePlotterTestCase(TextPlotterMixin, TestCase):
    pass


class SVGZPlotViewPlotterTestCase(BinaryPlotterMixin, TestCase):
    pass


class PNGPlotViewPlotterTestCase(BinaryPlotterMixin, TestCase):
    pass


class PNGPlotToFilePlotterTestCase(BinaryPlotterMixin, TestCase):
    pass


class PNGBase64PlotToValuePlotterTestCase(BinaryPlotterMixin, TestCase):
    pass


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
        buffer = self.plot.get_buffer()
        value = buffer.getvalue()
        self.assertEqual(value, self.output)


class BinaryBufferMixin(BaseBufferMixin):
    output = PLOT_BINARY
    file_type = "PNG"


class TextBufferMixin(BaseBufferMixin):
    output = PLOT_TEXT
    file_type = "SVG"


class SVGPlotToFileBufferTestCase(TextBufferMixin, TestCase):
    tclass = SVGPlotToFile


class SVGPlotToValueBufferTestCase(TextBufferMixin, TestCase):
    tclass = SVGPlotToValue


class SVGPlotViewBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = SVGZPlotView


class PNGPlotViewBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = PNGPlotView


class PNGPlotToFileBufferTestCase(BinaryBufferMixin, TestCase):
    tclass = PNGPlotToFile


class PNGBase64PlotToValueTestCase(BinaryBufferMixin, TestCase):
    tclass = PNGBase64PlotToValue


# TEST Explotation

# Storages

class BaseFileMixin:
    tclass = BasePlot
    filename = "filename"
    output: Any = ""

    def setUp(self):
        super().setUp()

        class MockPlot(self.tclass):
            def get_filename(self2):
                return self.filename

            def get_buffer(self2):
                self.buffer = self2.buffer_class()
                self.buffer.write(self.output)
                self.buffer.seek(0)
                return self.buffer

        self.patcher = patch('plottings.base.storages')
        self.storages = self.patcher.start()

        self.storage = MagicMock()
        self.storages.__getitem__.return_value = self.storage
        self.storage_save = Mock()
        self.storage.save = self.storage_save

        self.plot = MockPlot()

    def test_file(self):
        self.plot.save()
        self.storages.__getitem__.assert_called_with(self.plot.storage_name)
        self.storage_save.assert_called_with(self.filename,
                                             self.buffer)

    def tearDown(self):
        self.patcher.stop()


class PNGPlotToFileFileTestCase(BaseFileMixin, TestCase):
    tclass = PNGPlotToFile
    output = PLOT_BINARY


class SVGPlotToFileFileTestCase(BaseFileMixin, TestCase):
    tclass = SVGPlotToFile
    output = PLOT_TEXT


# Values

class BaseValueMixin:
    tclass = BasePlot
    filename = "filename"
    output: Any = ""

    def setUp(self):
        super().setUp()

        class MockPlot(self.tclass):
            def get_filename(self2):
                return self.filename

            def get_buffer(self2):
                self.buffer = self2.buffer_class()
                self.buffer.write(self.output)
                self.buffer.seek(0)
                return self.buffer

        self.plot = MockPlot()

    def decode_buffer(self, buffer):
        return buffer.getvalue()

    def test_value(self):
        value = self.plot.get_value()
        self.assertEqual(value.value, self.output)


class PNGPlotToBase64ValueTestCase(BaseValueMixin, TestCase):
    tclass = PNGBase64PlotToValue
    output = PLOT_BINARY

    def decode_buffer(self, buffer):
        value = super().decode_buffer(buffer)
        result = b64decode(str(value))
        return result


class SVGPlotToValueTestCase(BaseValueMixin, TestCase):
    tclass = SVGPlotToValue
    output = PLOT_TEXT
