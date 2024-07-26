# Django-Plottings

A library to generate Matplotlib graphics within Django applications.

Matplotlib is a Python library for mathematical graphics representations,
widely used in science in general and data science in particular.

Django is the leading framework for building web applications in the Python
ecosystem.

## About

This library is built with the intention of speeding up the building of data
science webapps by generating graphics on the server side.

The library provides three different ways to use the rendered graphics: 

 - as a view to be served as a standalone graphics file
 - as a text variable to be rendered within a webpage 
 - as a file to be saved and served lately

## Example

In the django `views.py` file:

```python

class PlotView(PNGPlotView):
    def get_data(self):
        return [(x.date, x.words) for x in Docs.objects.all()]

    @staticmethod
    def plotter_function(data):
        ...
        return fig
```


## Documentation

[Link](https://django-plottings.readthedocs.io/en/latest/) to Read the Docs.

## Good practices

Remember to disable graphics displays with `matplotlib.use('Agg')` in the
header of the plots file.

## Cache

As these tasks are computationally expensive is a good practice to cache them
once they are generated. This library is designed to integrate with the
Django's cache framework.


