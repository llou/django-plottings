
Tutorial
========

.. contents::
   :local:

KickStart
---------

Lets see how to insert a simple Matplotlib graph in a webpage using Django
Plottings.  Use the command ``pip`` to install the package to your local
development environment:

.. code::

   pip install django-plottings

Then add the module to the ``INSTALLED_APPS`` in the ``settings.py`` file of
your project.

.. code::

   INSTALLED_APPS = [
   ...
   'plottings',
   ...
   ]

Let's see how to render a plot to be passed to a template as context variable.
First we need to import Matplotlib and the PNGValue class of Django Plottings
to the ``views.py`` module of your app, and disable rendering to the screen:

.. code:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from plottings import PNGValuePlot
    from django.shortcuts import render
    matplotlib.use("Agg")
    
Then create the class that renders the plot:

.. code:: python

    class SimplePlotToValue(PNGValuePlot):
        def plotter_function(self, data, **kwargs):
            np.random.seed(2)
            fig, ax = plt.subplots()
            ax.plot(np.random.rand(20), '-o', ms=20, lw=2, alpha=0.7,
                    mfc='orange')
            ax.grid()
            return figure

    def plot(request, **kwargs):
        return render(request, "plot.html", {"plot": SimplePlotToValue()}

Setup the template ``plot.html`` in your apps template directory:

.. code::

      ...
      <body>
        <h1>My plot</h1>
        {{ plot }}
      </body>
      ...

And finally add a route to your plot view in your apps ``url.py``

.. code:: python

    from django.urls import path
    from . import views

    urlpatterns = [
        path("plot", views.plot, name="plot"),
        ]

Now you can run it from your Python environment:

.. code::
    
    ./manage.py runserver

And now open your browser and point it to your local app and then you should
view the plot in your screen.

How to build a Plot
-------------------

The plotting process is mainly done with the use of plotting classes each one
specialized in one type of output format and kind of rendering. Available
formats are two: **SVG** and **PNG** and they can be rendered as **View**,
**Value** or **File**, this gives us a family of six plotting classes: 

 - *PNGViewPlot*: A cached Django View class that returns a PNG.
 - *SVGViewPlot*: A cached Django View class that returns an SVGZ file.
 - *PNGFilePlot*: Returns a Django File object containing a PNG image to be
   saved to storage. Useful to run it in background jobs.
 - *SVGFilePlot*: Returnd a Django File object containing a SVGZ image to be
   saved to storage. Useful to run it in background jobs.
 - *PNGValuePlot*: A cached python variable containing a plot object ready to be
   rendered within a template as a PNG image encoded in *Base64*.
 - *SVGValuePlot*: A cached python variable containing a plot object ready to be
   rendered within a template as an inlined SVG image.

These classes share all the same plotting methods that are:
 
 - An static method ``plotter_function(data, **options)``, that returns a
   Matplotlib ``figure`` object. The idea is not to implement the function here
   but to bring it from an interactive development environment like iPython
   Jupyter Notebooks.
 - A method ``get_plot_data()`` that is used to provide data to the
   ``plotter_function()``.
 - Another method ``get_plot_options()`` that returns a dictionary of values
   ready to be passed as named arguments to the ``plotter_function()`` to
   customize its behaviour.

So to build a graph you have to first select the plotting class you want to use
then copy&paste the ``plotter_function()`` and refactor it to obtain data from
the ``data`` parameter and personalization from the named arguments.

Then implement how to obtain the data from Django models or whatever and build
the ``get_plot_data()`` and collect the options with ``get_plot_options()``.
These steps might be different in a **View** class than in the **Value** and
**File** classes.

How to build a View
-------------------

Django Views are initialized each request and values are stored in the object
as the object attributes ``request``, ``args``, ``kwargs``. So the methods
``get_plot_options()`` and ``get_plot_data()`` must access these three
attributes to build a response plot.

.. code:: python

    class ActivitiesPlot(PNGViewPlot):

        def get_plot_options(self):
            return {"color": request.GET.get("color", "blue")}

        def get_plot_data(self):
            activities = self.request.user.get_activities()
            return [ x.date for x in activities ]
        

How to build a Value
--------------------

The **Value** class should be declared with the ``__init__()`` initialization
method with the parameters needed to set the object attributes required by
the ``get_plot_data()`` and ``get_plot_options()`` to pass the right parameters
to the plotting function to render the image accordingly.

.. code:: python

    class ActivitiesPlot(PNGValuePlot):

        def __init__(self, activities, color="blue"):
            self.activities = activities
            self.color = color

        def get_plot_options(self):
            return {"color": self.color}

        def get_plot_data(self):
            return [ x.date for x in self.activities ]

Then the class is initialized within the view function or
``get_context_data()`` of the View object. The resulting plot object is passed
to the template as another value to be rendered.

.. code:: python

    def activities_view(request, *args, **kwargs):
        activities = request.user.get_activities()
        a_plot = ActivitiesPlot(activities)
        return render(request, "activities.html", {"a_plot": a_plot})


How to build and Save a File
----------------------------

The **File** class should be declared with the ``__init__()`` initialization
method with the parameters needed to set the object attributes required by
the ``get_plot_data()`` and ``get_plot_options()`` to pass the right parameters
to the plotting function to render the image accordingly.

.. code:: python

    class ActivitiesPlot(PNGFilePlot):

        def __init__(self, activities, color="blue"):
            self.activities = activities
            self.color = color

        def get_plot_options(self):
            return {"color": self.color}

        def get_plot_data(self):
            return [ x.date for x in self.activities ]

To render the plot when its needed you just have to call the object with the
and asign it to a model field and then save it to store the plot in storage
and the reference to it in the database:

.. code:: python

    def task_save_activities(user_id):
        user = User.objects.get(id=user_id)
        activities = user.get_activities()
        a_plot = ActivitiesPlot(activities)
        user.activities_plot = a_plot.as_file()
        user.save()

Caching
-------

Caching is implemented in the **View** and **Value** classes. You only need to
implement the ``get_cache_key()`` method that returns an identifying value of
your plot and to set the timeout you have to set the class attribute
``cache_timeout`` to the number of seconds of your choosing.

.. code:: python

    class ActivitiesPlot(PNGViewPlot):
        cache_timeout = 60 * 60 * 24

        def get_cache_key(self):
            return f"activities_plot_{self.request.user.id}"


Post Processing
---------------

To modify the rendered image there is the ``process_image()`` method that takes
an image in memory file and returns another.

Good Practices
--------------

It's a good idea to have the code split in separated files in the Django app
directory. The initial propossal is to place all matplotlib, numpy, pandas...
code in ``plots.py`` file. 

And don't forget to ``matplotlib.use("Agg")``.
