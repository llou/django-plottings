import os
from typing import Any
from contextlib import contextmanager
from unittest.mock import patch, MagicMock
from django.test import TestCase
from plottings.base import BasePlot
from plottings import (
        CachedPNGPlotView,
        CachedSVGZPlotView,
        CachedSVGPlotToValue,
        CachedPNGBase64PlotToValue,
        CachedSVGZPlotToFile,
        CachedPNGPlotToFile,
        )

os.environ['DJANGO_SETTINGS_MODULE'] = "plottings.tests.test_settings"


class MockFigure:
    def __init__(self, mock_image):
        self.mock_image = mock_image

    def savefig(self, output_buffer, **kwargs):
        output_buffer.write(self.mock_image)


class CacheTestMixin:
    tclass = BasePlot
    cache_keys = [1, 1, 2]
    outputs: Any = [b"1", b"1", b"3"]

    def setUp(self):
        class Mock(self.tclass):
            def __init__(self2, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.counter = 0

            def get_cache_key(self2):
                return self.cache_keys[self.counter]

            @contextmanager
            def _get_figure(self2):
                yield MockFigure(self.outputs[self.counter])

            def get_image(self2):
                image = super().get_image()
                self.counter += 1
                return image

        self._cache = {}

        def get(key, default=None):
            return self._cache.get(key, default)

        def _set(key, value, timeout=60):
            self._cache[key] = value

        cache = MagicMock()
        cache.get = get
        cache.set = _set

        self.patcher = patch("plottings.base.caches")
        self.caches_mock = self.patcher.start()
        self.caches_mock.__getitem__.return_value = cache

        self.plot = Mock()

    def test_uno(self):
        image1 = self.plot.get_image()
        self.assertEqual(self.outputs[0], image1.getvalue())
        self.assertEqual(self._cache[1], self.outputs[0])
        image2 = self.plot.get_image()
        self.assertEqual(self.outputs[1], image2.getvalue())
        image3 = self.plot.get_image()
        self.assertEqual(self.outputs[2], image3.getvalue())
        self.assertEqual(self._cache[2], self.outputs[2])

    def tearDown(self):
        self.patcher.stop()


class PNGPlotViewTestCase(CacheTestMixin, TestCase):
    tclass = CachedPNGPlotView


class SVGZPlotViewTestCase(CacheTestMixin, TestCase):
    tclass = CachedSVGZPlotView


class SVGPlotToValueTestCase(CacheTestMixin, TestCase):
    tclass = CachedSVGPlotToValue
    outputs = ["1", "1", "3"]


class PNGBase64PlotToValueTestCase(CacheTestMixin, TestCase):
    tclass = CachedPNGBase64PlotToValue


class SVGZPlotToFileTestCase(CacheTestMixin, TestCase):
    tclass = CachedSVGZPlotToFile


class PNGPlotToFileTestCase(CacheTestMixin, TestCase):
    tclass = CachedPNGPlotToFile
