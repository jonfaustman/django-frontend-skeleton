Django Frontend Skeleton documentation
======================================

Django Frontend Skeleton is a basic Django template skeleton built on `HTML5 Boilerplate <https://github.com/h5bp/html5-boilerplate>`_ and `Twitter Bootstrap <https://github.com/twitter/bootstrap>`_.

With the convenience of an installable Django application, create custom templates built on top of one of the most well-known, widespread templates (HTML5 Boilerplate) and a robust front-end framework (Twitter Bootstrap.)

Version 2.0.0 of Django Frontend Skeleton is a much simpler package - it's now just a small extended 'skeleton' template, which requires Django Frontend. No more duplication!

:Package: `https://pypi.python.org/pypi/django-frontend-skeleton <https://pypi.python.org/pypi/django-frontend-skeleton>`_
:Source: `https://github.com/jonfaustman/django-frontend-skeleton <https://github.com/jonfaustman/django-frontend-skeleton>`_

Starring
---------
* `HTML5 Boilerplate (based on 4.2.0) <https://github.com/h5bp/html5-boilerplate>`_
* `Modernizr (2.6.2) <https://github.com/Modernizr/Modernizr>`_
* `jQuery (1.10.2) and (2.0.3) <https://github.com/jquery/jquery>`_
* `Twitter Bootstrap (3.0.0) <https://github.com/twbs/bootstrap>`_
* `iOS-Orientationchange-Fix <https://github.com/scottjehl/iOS-Orientationchange-Fix>`_

Getting Started
-----------------

Install
~~~~~~~~
1. install `django-frontend-skeleton` (pip install, add to your requirements files, etc.)
2. add `'djfrontend'` and `'djfrontend.skeleton'` to your INSTALLED_APPS
3. make sure `'django.contrib.staticfiles'` is also in your INSTALLED_APPS

Extend
~~~~~~~
Extend the skeleton's base template in your template(s)
::

    {% extends 'djfrontend/skeleton.html' %}

Load
~~~~~~
Load all the djfrontend tags if you want to add or change the template's defaults.
::

    {% load djfrontend %}


Template Blocks
----------------
Template blocks provided by Django Frontend which are fundamental for Django Frontend Skeleton.

djfrontend_h5bp_css
~~~~~~~~~~~~~~~~~~~~~
Block to include {% djfrontend_normalize %} and/or {% djfrontend_h5bp_css %}.

djfrontend_twbs_css
~~~~~~~~~~~~~~~~~~~~~
Block to override the included Twitter Bootstrap CSS and responsive CSS files.

djfrontend_twbs_js
~~~~~~~~~~~~~~~~~~~~
Override the included {% djfrontend_twbs_js %}.

Further Documentation
----------------------
For more documenation about Django Frontend `read the documentation <https://django-frontend.readthedocs.org/>`_.

Contents
---------

.. toctree::
   :maxdepth: 2
   
   license
   changelog