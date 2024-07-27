
Django-Plottings Documentation
==============================

.. contents::
   :local:

Django-Plottings is a library that merge two of the most emblematic Python
projects by providing three means of generating graphics from the data managed
by the web applications framework:

 - A **view** to serve the graphic file. 
 - A **value** to be passed to the template framework to integrate the graphic
   inside a webpage.
 - A **file** to be stored in a media folder to be accessed later.

The idea behind this project is to provide a fast way to pass from analysis
using a Jupyter Notebook to a production environment using the Django
framework.

It also can be used in combination with Alpine.js_, htmlx_ or Unpoly_ as a
substitution for client side graphics rendering, to provide some interactivity
in the plotting of data. 

.. _Alpine.js: https://alpinejs.dev
.. _htmlx: https://htmlx.org
.. _Unpoly: https://unpoly.com

Other great advantage of this system is that the plot data never leaves the
machine so it can't be scrapped.

It renders graphics in two different formats PNG and SVG, the first a concise
but not much precise way of storing images, the second much more precise in the
details but heavier.

Base Classes
------------

Django-Plottings is intended to work in a similar manner of the Django class 
based views by subclassing and overriding methods that provide the functionality
required to build the plots.

The commom methods to be subclassed are:

 - **get_data()**: That contain all the logic required to provide the plotting
   function with data.

 - **get_kwargs()**: That provide the plotting function with extra parameters
   for customizing the way the plot is built.

 - **plotter_function**: That gets the data and the parameter and returns a
   figure object ready to be dumped in the formats required by the building
   class.


View Classes
------------

These classes are a mixture of Django views and Plottings base object so
parameters are added to the class by the `setup()` method and accesible from
the class instance.

They work as other class based view by passing the to the `path()` function
calling the `as_view()` method.

PNGPlotView
^^^^^^^^^^^

.. autoclass:: plottings.PNGPlotView
   :members:
   :inherited-members:

SVGZPlotView
^^^^^^^^^^^^

.. autoclass:: plottings.SVGZPlotView
   :members:
   :inherited-members:

File Classes
------------

These two classes are intended to be initiallized and then to proceed to call
the `get_file()` method that returns a Django file object ready to be assigned
to a Django ImageField for saving and storing the data in a media folder.

PNGPlotToFile
^^^^^^^^^^^^^

.. autoclass:: plottings.PNGPlotToFile
   :members:
   :inherited-members:

SVGZPlotToFile
^^^^^^^^^^^^^^

.. autoclass:: plottings.SVGZPlotToFile
   :members:
   :inherited-members:

Value Classes
-------------

This two classes are intended to be initiallized and then to proceed to call
the `get_value()` method that returns a ValueItem object intended to be passed
to the Django Template System to render the webpage with the image included.

PNGBase64PlotToValue
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: plottings.PNGBase64PlotToValue
   :members:
   :inherited-members:

.. autoclass:: plottings.base.B64ValueItem

SVGPlotToValue
^^^^^^^^^^^^^^

.. autoclass:: plottings.SVGPlotToValue
   :members:
   :inherited-members:

.. autoclass:: plottings.base.ValueItem
