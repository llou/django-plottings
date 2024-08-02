
Development
===========

.. contents::
   :local:

You are welcome to make contributions to this project. The project main page
is at Github_.

.. _Github: https://github.com/llou/django-plottings


Code Structure
--------------

The main ren

 - ``/base.py``:
 - ``/file.py``
 - ``/value.py``
 - ``/views.py``

Testing the App
---------------

This software is tested using a Django testing application that is stored in
the ``/testing_app`` directory. It provides two main features:

 - A tool for running the project test suite
 - A running webapp to test the results.

To run it only requires to install the ``requirements.txt`` in a virtualenv and
with it activated launch ``manage.py runserver`` for running the test server
and ``manage.py test`` to launch the testsuite.
