
Development
===========

.. contents::
   :local:

You are welcome to make contributions to this project. The project main page
is at Github_.

.. _Github: https://github.com/llou/django-plottings


Code Structure
--------------

.. automodule:: plottings.base

.. autoclass:: plottings.base.BasePlot
.. autoclass:: plottings.base.CachedMixin
.. autoclass:: plottings.base.SVGPlotMixin
.. autoclass:: plottings.base.SVGZPlotMixin
.. autoclass:: plottings.base.PNGPlotMixin

.. automodule:: plottings.views
.. autoclass:: plottings.views.BasePlotView
.. autoclass:: plottings.views.CachedMixin

.. automodule:: plottings.value
.. autoclass:: plottings.value.ValueMixin
.. autoclass:: plottings.value.Base64ValueMixin

.. automodule:: plottings.file
.. autoclass:: plottings.file.FileMixin

Testing Application
-------------------

This software is tested using a Django testing application that is stored in
the ``/testing_app`` directory. It provides two main features:

 - A tool for running the project test suite
 - A running webapp to test the results.

To run it only requires to install the ``requirements.txt`` in a virtualenv and
with it activated launch ``./manage.py runserver`` for running the test server
and ``./manage.py test`` to launch the testsuite.
