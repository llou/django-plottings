# Django-Plottings

A library to generate Matplotlib graphics within Django applications.

Matplotlib is a Python library for mathematical graphics represaentations,
widely used in science in general and data science in particular.

Django is the leading framework for building web applications in the Python
ecosystem.

The library provides three different ways to use the rendered graphics: 

 - as a view to be viewed or included in a webpage
 - as a text variable to be rendered within a template 
 - as a file to be saved in a media directory

## Examples

In the django `views.py` file:

```python

class PlotView(PNGPlotView):
    def get_data(self):
        return [(x.date, x.words) for x in Docs.objects.all()]

    @staticmethod
    def plotter_function(data, color='blue'):
        plotter_exampe
```



## Documentation

Link to read the docs.

## Good practices

This library is very opinionated on how graphics should be built.

### Split data and graphics

Split data analysis in `data.py` and graphic drawing in `plots.py`. Remember to
disable graphics displays with `matplotlib.use('Agg')` in the header of the
graphics file.

## Cache

As these tasks are computationally expensive is a good practice to cache them
once they are generated.  This library is designet to integrate under the
Django's cache framework.


