from django.urls import path
from . import views

urlpatterns = [
        path("", views.main, name="main"),
        path("activity.png", views.PNGActivityPlot.as_view(), name="png"),
        path("activity.svgz", views.SVGZActivityPlot.as_view(), name="svgz"),
        path("new_png", views.new_png, name="new_png"),
        path("new_svg", views.new_svg, name="new_svg"),
    ]
