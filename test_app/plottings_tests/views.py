from random import randrange
from datetime import date, timedelta
from django.shortcuts import render
from plottings.plots.activity import ActivityMap
from plottings import (
        SVGZPlotToFile,
        PNGPlotToFile,
        PNGPlotView,
        SVGZPlotView,
        SVGPlotToValue,
        PNGBase64PlotToValue,
        )
from .plots import activity_plot
from .models import Plot


class ActivityPlotMixin:
    plotter_function = staticmethod(activity_plot)
    activity_class = ActivityMap
    filename = "activity.svg"
    number_of_events = 400
    period = 365

    def random_activity(self):
        result = []
        today = date.today()
        for _ in range(self.number_of_events):
            td = timedelta(randrange(self.period))
            result.append(today - td)
        return result

    def __init__(self, **kwargs):
        self.map = self.activity_class(date.today())
        self.map.load_activity(self.random_activity())

    def get_plot_kwargs(self):
        return {"xticks": self.map.get_x_ticks(),
                "yticks": self.map.get_y_ticks(),
                }

    def get_data(self):
        return self.map.get_data()


class SVGPlot(ActivityPlotMixin, SVGPlotToValue):
    plotter_function = staticmethod(activity_plot)


class PNGPlot(ActivityPlotMixin, PNGBase64PlotToValue):
    plotter_function = staticmethod(activity_plot)


class PNGActivityPlot(ActivityPlotMixin, PNGPlotView):
    plotter_function = staticmethod(activity_plot)


class SVGZActivityPlot(ActivityPlotMixin, SVGZPlotView):
    plotter_function = staticmethod(activity_plot)


def main(request):
    plots = Plot.objects.all()
    context = {"svg_data": SVGPlot().get_value(),
               "png_data": PNGPlot().get_value(),
               "plots": plots}

    return render(request, "main.html", context)


class SVGZPlotToFile(ActivityPlotMixin, SVGZPlotToFile):
    plotter_function = staticmethod(activity_plot)


class PNGPlotToFile(ActivityPlotMixin, PNGPlotToFile):
    plotter_function = staticmethod(activity_plot)


def new_png(request):
    data = SVGZPlotToFile().get_buffer()
    plot = Plot()
    return ""


def new_svg(request):
    return ""
