
Reference
=========

.. contents::
   :local:

Base Classes
------------

Django-Plottings is intended to work in a similar manner of the Django class 
based views by subclassing and overriding methods that provide the functionality
required to build the plots.

The commom methods to be subclassed are:

 - ``get_plot_data()``: That contain all the logic required to provide
   ``plotter_function`` with data.

 - ``get_plot_options()``: That provide the plotting function with extra
   parameters for customizing the way the plot is built.

 - ``plotter_function(data, **options)``: That gets the data and the parameters
   and returns a figure object ready to be dumped in the formats required by
   the building class.

View Classes
------------

These classes are a mixture of Django views and Plottings base object so
parameters are added to the class by the ``setup()`` method and accesible from
the class instance.

They work as other class based view by passing the to the ``path()`` function
calling the ``as_view()`` method.

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
the ``get_file()`` method that returns a Django file object ready to be assigned
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

Both classes work the same way: first initialization of the class for then call
the ``get_value()`` method that returns a variable intended to be passed to the
Django Template System to render the webpage with the image included.

PNGBase64PlotToValue
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: plottings.PNGBase64PlotToValue
   :members:
   :inherited-members:

SVGPlotToValue
^^^^^^^^^^^^^^

.. autoclass:: plottings.SVGPlotToValue
   :members:
   :inherited-members:
