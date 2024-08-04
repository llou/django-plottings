
Contributing
============

.. contents::
   :local:

You are welcome to make contributions to this project. The project main page
is at Github_.

.. _Github: https://github.com/llou/django-plottings


Class Architecture
------------------
The classes in this project are built by composing a base class, ``BasePlot``
with different mixins to in the end provide full featured classes ready for
production.

.. automodule:: plottings.base

.. autoclass:: plottings.base.BasePlot
   :members:
.. autoclass:: plottings.base.CachedMixin
   :members:
.. autoclass:: plottings.base.SVGPlotMixin
   :members:
.. autoclass:: plottings.base.SVGZPlotMixin
   :members:
.. autoclass:: plottings.base.PNGPlotMixin
   :members:

.. automodule:: plottings.views
.. autoclass:: plottings.views.BasePlotView
   :members:

.. automodule:: plottings.value
.. autoclass:: plottings.value.ValueMixin
   :members:
.. autoclass:: plottings.value.Base64ValueMixin
   :members:

.. automodule:: plottings.file
.. autoclass:: plottings.file.FileMixin
   :members:

Testing Application
-------------------

This software is tested using a Django testing application that is stored in
the ``/testing_app`` directory. It provides two main features:

 - A tool for running the project test suite
 - A running webapp to test the results.

To run it only requires to install the ``requirements.txt`` in a virtualenv and
with it activated launch ``./manage.py runserver`` for running the test server
and ``./manage.py test`` to launch the testsuite.
