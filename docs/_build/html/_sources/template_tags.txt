Template tags
==============
Use the included template tags to suit your needs.

There are skeleton, HTML5 Boilerplate and Twitter Bootstrap specific template tags, so load the template tag set that you're wanting to use.

skeleton
---------
::

    {% load skeleton %}

skeleton_ios_fix
~~~~~~~~~~~~~~~~~
Returns the iOS-Orientationchange-Fix.
::

    <script>/*! A fix for the iOS orientationchange zoom bug. Script by @scottjehl, rebound by @wilto.MIT / GPLv2 License.*/(function(a){function m(){d.setAttribute("content",g),h=!0}function n(){d.setAttribute("content",f),h=!1}function o(b){l=b.accelerationIncludingGravity,i=Math.abs(l.x),j=Math.abs(l.y),k=Math.abs(l.z),(!a.orientation||a.orientation===180)&&(i>7||(k>6&&j<8||k<8&&j>6)&&i>5)?h&&n():h||m()}var b=navigator.userAgent;if(!(/iPhone|iPad|iPod/.test(navigator.platform)&&/OS [1-5]_[0-9_]* like Mac OS X/i.test(b)&&b.indexOf("AppleWebKit")>-1))return;var c=a.document;if(!c.querySelector)return;var d=c.querySelector("meta[name=viewport]"),e=d&&d.getAttribute("content"),f=e+",maximum-scale=1",g=e+",maximum-scale=10",h=!0,i,j,k,l;if(!d)return;a.addEventListener("orientationchange",m,!1),a.addEventListener("devicemotion",o,!1)})(this);</script>
    
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
Returns jQuery JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback. The latest '1.9.1' is the default and is included.
::

    <script src="/static/skeleton/js/h5bp/jquery/1.9.1/jquery.js"></script>

Or

::

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/skeleton/js/h5bp/jquery/1.9.1/jquery.min.js"><\/script>')</script>

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
Returns Twitter Bootstrap (2.3.2) JavaScript file(s). all returns concatenated file; full file for TEMPLATE_DEBUG, minified otherwise. Other choices include:

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