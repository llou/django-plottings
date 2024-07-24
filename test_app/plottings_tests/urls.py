from django.urls import path
from . import views

urlpatterns = [
        path("", views.view, name="view"),
        path("activity.png", views.PNGActivityPlot.as_view(), name="png"),
        path("activity.svgz", views.SVGZActivityPlot.as_view(), name="svgz"),
    ]
