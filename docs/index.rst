
Django-Plottings Documentation
==============================

.. toctree::
   :maxdepth: 1

   tutorials
   reference
   development

Introduction
------------

Django Plottings is a library for using Matplotlib_ graphing library within the
`Django Web Framework`_. It can be used to produce plots in three different
ways:

.. _Matplotlib: https://matplotlib.org/stable/
.. _Django Web Framework: https://www.djangoproject.com/

 - As a **view** that responds to clients request, to serve the plot alone.
 - As a **value** to be inserted in a web page template, to serve the plot as part 
   of a webpage.
 - As a **file** saved to storage for background processing.

The idea behind this project is to provide a fast way to go from data analysis
to production using Django framework, proposing an opinionated way of building
the graphs similar to those of Django class based views. The lifecycle of the
graph is as follows:

.. .. image:: steps.svg

It includes integration with the Django cache so plots don't need to be
regenerated every time the same graph is requested. It also provides an step
for post processing the graphs after rendering but before caching to add a
watermark or whatever.

This tool is focused in high-quality rendering graphics, it is not a very
performant solution, if you need high speed rendering there are other tools
more suitable for this purpose.

Server Side Rendering
---------------------

This solution build the graphics on the server an alternative to rendering
graphs in the browser and this has its advantages:

 - Data never leves the server.
 - More resources available for rendering.
 - No need for front end programing.
 - No need for a full featured web browser for rendering.

And its drawbacks:
 
 - More computing power to render the requests.
 - More memory required for each server thread.
 - Non interactive graphs.


Compatibility
-------------

This module currently supports two file formats PNG and SVG.  The compatibility
is not fully checked, it runs with the lastest versions of Django 5.0, Numpy
2.0, Matplotlib 3.9 and Python 3.12.4.

It has been tested in Linux and Mac OS environments but should run on Windows
as well.

About
-----

This is project is originated as a side project of `Jorge Monforte González`_.

.. _Jorge Monforte González: yo@llou.net

Project pages:

 - Github: https://github.com/llou/django-plottings
 - PyPI: https://pypi.org/project/django-plottings/
 - Documentation: https://django-plottings.readthedocs.io/en/latest/
