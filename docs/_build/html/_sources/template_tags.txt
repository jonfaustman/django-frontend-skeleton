Template tags
==============
Use the included template tags to suit your needs.

There are HTML5 Boilerplate and Twitter Bootstrap specific template tags, so load the template tag set that you're wanting to use.

HTML5 Boilerplate
-------------------
::

    {% load h5bp %}

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

    <link rel="stylesheet" href="/static/skeleton/css/h5bp/normalize.css">

h5bp_css
~~~~~~~~~
Returns HTML5 Boilerplate CSS file.
::

    <link rel="stylesheet" href="/static/skeleton/css/h5bp/h5bp.css">

h5bp_modernizr
~~~~~~~~~~~~~~~
Returns Modernizr JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file. The latest '2.6.2' is the default and is included.
::

    <script src="/static/skeleton/js/h5bp/modernizr/2.6.2/modernizr.js"></script>

Or

::

    <script src="/static/skeleton/js/h5bp/modernizr/2.6.2/modernizr.min.js"></script>

h5bp_jquery
~~~~~~~~~~~~
Returns jQuery JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback. The latest '1.9.0' is the default and is included.
::

    <script src="/static/skeleton/js/h5bp/jquery/1.9.0/jquery.js"></script>

Or

::

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/skeleton/js/h5bp/jquery/1.9.0/jquery.min.js"><\/script>')</script>

h5bp_ga
~~~~~~~~
Returns Google Analytics asynchronous snippet if TEMPLATE_DEBUG is not set.
::

    <script>var _gaq=[["_setAccount","UA-XXXXX-X"],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src=("https:"==location.protocol?"//ssl":"//www")+".google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>

Twitter Bootstrap
------------------
::

    {% load bootstrap %}

bootstrap_css
~~~~~~~~~~~~~~
Returns Twitter Bootstrap CSS file. TEMPLATE_DEBUG returns full file, otherwise returns minified file.
::

    <link rel="stylesheet" href="/static/skeleton/css/bootstrap/bootstrap.css">

Or

::

    <link rel="stylesheet" href="/static/skeleton/css/bootstrap/bootstrap.min.css">

bootstrap_responsive_css
~~~~~~~~~~~~~~~~~~~~~~~~~
Returns Twitter Bootstrap responsive CSS file. TEMPLATE_DEBUG returns full file, otherwise returns minified file.
::

    <link rel="stylesheet" href="/static/skeleton/css/bootstrap/bootstrap-responsive.css">

Or

::

    <link rel="stylesheet" href="/static/skeleton/css/bootstrap/bootstrap-responsive.min.css">

bootstrap_js
~~~~~~~~~~~~~
Returns Twitter Bootstrap (2.2.2) JavaScript file(s). all returns concatenated file; full file for TEMPLATE_DEBUG, minified otherwise. Other choices include:

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
* typeahead

Individual files are not minified.

{% boostrap_js all %} would render
::

    <script src="/static/skeleton/js/bootstrap/bootstrap.js"></script>

Or

::

    <script src="/static/skeleton/js/bootstrap/bootstrap.min.js"></script>

{% bootstrap_js alert affix %} would render
::

    <script src="/static/skeleton/js/bootstrap/bootstrap-affix.js"></script>
    <script src="/static/skeleton/js/bootstrap/bootstrap-alert.js"></script>

Shout out to Ryan Brady and his `Django Bootstrapped <https://github.com/rbrady/django-bootstrapped>`_ for inspiration and initial code.