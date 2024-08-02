from random import randrange
from datetime import date, timedelta
from django.shortcuts import render
from plottings import (
        SVGZPlotToFile,
        PNGPlotToFile,
        PNGPlotView,
        SVGZPlotView,
        SVGPlotToValue,
        PNGBase64PlotToValue,
        )
from django.http import HttpResponseRedirect
from django.urls import reverse
from .plots import activity_plot
from .data import ActivityMap
from .models import Plot


class ActivityPlotMixin:
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

    def get_plot_options(self):
        return {"xticks": self.map.get_x_ticks(),
                "yticks": self.map.get_y_ticks(),
                }

    def get_plot_data(self):
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
    context = {"svg_data": SVGPlot(),
               "png_data": PNGPlot(),
               "plots": plots}

    return render(request, "main.html", context)


class PNGFilePlot(ActivityPlotMixin, PNGPlotToFile):
    plotter_function = staticmethod(activity_plot)


def new_png(request):
    file = PNGFilePlot().get_file()
    plot = Plot(plot=file)
    plot.save()
    return HttpResponseRedirect(reverse('main'))


class SVGZFilePlot(ActivityPlotMixin, SVGZPlotToFile):
    plotter_function = staticmethod(activity_plot)


def new_svg(request):
    file = SVGZFilePlot().get_file()
    plot = Plot(plot=file)
    plot.save()
    return HttpResponseRedirect(reverse('main'))
