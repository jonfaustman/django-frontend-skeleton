========================
Django Frontend Skeleton
========================

A basic Django template skeleton built on HTML5 Boilerplate and Twitter Bootstrap.

---------
Starring
---------
* `HTML5 Boilerplate <https://github.com/h5bp/html5-boilerplate>`_
    - `Modernizr <https://github.com/Modernizr/Modernizr>`_
* `Twitter Bootstrap <https://github.com/twitter/bootstrap>`_
* `jQuery <https://github.com/jquery/jquery>`_
* `iOS-Orientationchange-Fix <https://github.com/scottjehl/iOS-Orientationchange-Fix>`_

----------------
Getting Started
----------------

Install
========
1. install `django-frontend-skeleton` (pip install, add to your requirements files, etc.)
2. add `'django-frontend-skeleton'` to your INSTALLED_APPS

Extend
=======
Extend the skeleton's base template in your template(s)
::

    {% extends 'skeleton/base.html' %}

Template tags
==============
Use the included template tags to suit your needs.

~~~~~~~~~~~~~~~
{% load h5bp %}
~~~~~~~~~~~~~~~

h5bp_html
~~~~~~~~~~
Returns HTML tag according to chosen language - 'en' is the default.
::

    <!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
    <!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
    <!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->

h5bp_normalize
~~~~~~~~~~~~~~~
Returns Normalize CSS file.
::

    <link rel="stylesheet" href="/static/css/h5bp/normalize.css">

h5bp_css
~~~~~~~~~
Returns HTML5 Boilerplate CSS file.
::

    <link rel="stylesheet" href="/static/css/h5bp/h5bp.css">

h5bp_modernizr
~~~~~~~~~~~~~~~
Returns Modernizr JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file. The latest '2.6.2' is the default and is included.
::

    <script src="/static/js/h5bp/modernizr/2.6.2/modernizr.js"></script>

Or
::

    <script src="/static/js/h5bp/modernizr/2.6.2/modernizr.min.js"></script>

h5bp_jquery
~~~~~~~~~~~~
Returns jQuery JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback. The latest '1.8.2' is the default and is included.
::

    <script src="/static/js/h5bp/jquery/1.8.2/jquery.js"></script>

Or
::

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/h5bp/jquery/1.8.2/jquery.min.js"><\/script>')</script>

h5bp_ga
~~~~~~~~
Returns Google Analytics asynchronous snippet if TEMPLATE_DEBUG is not set.
::

    <script>var _gaq=[["_setAccount","UA-XXXXX-X"],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src=("https:"==location.protocol?"//ssl":"//www")+".google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>

~~~~~~~~~~~~~~~~~~~~~
{% load bootstrap %}
~~~~~~~~~~~~~~~~~~~~~

bootstrap_css
~~~~~~~~~~~~~~
Returns Twitter Bootstrap CSS file. TEMPLATE_DEBUG returns full file, otherwise returns minified file.
::

    <link rel="stylesheet" href="/static/css/bootstrap/bootstrap.css">

Or
::

    <link rel="stylesheet" href="/static/css/bootstrap/bootstrap.min.css">

bootstrap_responsive_css
~~~~~~~~~~~~~~~~~~~~~~~~~
Returns Twitter Bootstrap responsive CSS file. TEMPLATE_DEBUG returns full file, otherwise returns minified file.
::

    <link rel="stylesheet" href="/static/css/bootstrap/bootstrap-responsive.css">

Or
::

    <link rel="stylesheet" href="/static/css/bootstrap/bootstrap-responsive.min.css">

bootstrap_js
~~~~~~~~~~~~~
Returns Twitter Bootstrap (2.2.1) JavaScript file(s). all returns concatenated file; full file for LOCAL, minified otherwise. Other choices include:

* affix
* alert
* button
* carousel
* collapse
* dropdown
* modal
* popover (adds tooltip if not included)
* scrollspy
* tab
* tooltip
* transition
* typehead

Individual files are not minified.

{% boostrap_js all %} would render
::

    <script src="/static/js/bootstrap/bootstrap.js"></script>

Or
::

    <script src="/static/js/bootstrap/bootstrap.min.js"></script>

{% bootstrap_js alert affix %} would render
::

    <script src="/static/js/bootstrap/bootstrap-affix.js"></script>
    <script src="/static/js/bootstrap/bootstrap-alert.js"></script>

Shout out to Ryan Brady and his `Django Bootstrapped <https://github.com/rbrady/django-bootstrapped>`_ for inspiration and initial code.

---------
License
---------
MIT License

Component Specific Licenses:
==============================
* HTML5 Boilerplate: MIT License
* Modernizr: BSD/MIT License
* Twitter Bootstrap: Apache License, Version 2.0
* jQuery: MIT/GPL License
* iOS-Orientationchange-Fix: MIT/GPL v2.0 License