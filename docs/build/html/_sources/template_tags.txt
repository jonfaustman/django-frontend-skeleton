Template tags
==============
Use the included djfrontend template tags to suit your needs.

djfrontend
-----------
::

    {% load djfrontend %}

djfrontend_h5bp_html
~~~~~~~~~~~~~~~~~~~~~
Returns HTML tag according to chosen language - 'en' is the default.
::

    <!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
    <!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
    <!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->

djfrontend_h5bp_css
~~~~~~~~~~~~~~~~~~~~~
Returns HTML5 Boilerplate CSS file according to version number. The latest '4.2.0' is included.
::

    <link rel="stylesheet" href="/static/djfrontend/css/h5bp/4.2.0/h5bp.css">

djfrontend_normalize
~~~~~~~~~~~~~~~~~~~~~
Returns Normalize CSS file according to version number. The latest '1.1.1' is included.
::

    <link rel="stylesheet" href="/static/djfrontend/css/normalize/1.1.1/normalize.css">

djfrontend_fontawesome
~~~~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns Font Awesome CSS file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file.
::

    <link rel="stylesheet" href="/static/djfrontend/css/fontawesome/3.2.1/font-awesome.css">

Or

::

    <link rel="stylesheet" href="/static/djfrontend/css/fontawesome/3.2.1/font-awesome.min.css">

djfrontend_fontawesome_ie
~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns Font Awesome IE7 CSS file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file.
::

    <link rel="stylesheet" href="/static/djfrontend/css/fontawesome/3.2.1/font-awesome-ie7.css">

Or

::

    <link rel="stylesheet" href="/static/djfrontend/css/fontawesome/3.2.1/font-awesome.min-ie7.css">

djfrontend_modernizr
~~~~~~~~~~~~~~~~~~~~~
Returns Modernizr JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local callback. The latest '2.6.2' is included.
::

    <script src="/static/djfrontend/js/modernizr/2.6.2/modernizr.js"></script>

Or

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/modernizr/%s/modernizr.min.js"></script>' % v,
    <script>window.Modernizr || document.write(\'<script src="static/djfrontend/js/modernizr/2.6.2/modernizr.min.js"><\/script>\')</script>

djfrontend_jquery
~~~~~~~~~~~~~~~~~~
Returns jQuery JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback. The latest '1.10.2' and '2.0.3' is included.
::

    <script src="/static/djfrontend/js/jquery/1.10.2/jquery.js"></script>

Or

::

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/djfrontend/js/jquery/1.10.2/jquery.min.js"><\/script>')</script>

djfrontend_jqueryui
~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns jQuery UI plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback.
::

    <script src="/static/djfrontend/js/jquery/jqueryui/1.10.3/jquery-ui.js"></script>

Or

::

    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>' % v,
    <script>window.jQuery.ui || document.write(\'<script src="/static/djfrontend/js/jquery/jqueryui/1.10.3/jquery-ui.min.js"><\/script>\')</script>

djfrontend_jquery_datatables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns the jQuery DataTables plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback.
::

    <script src="/static/djfrontend/js/jquery/jquery.dataTables/1.9.4/jquery.dataTables.js"></script>

Or

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/datatables/1.9.4/jquery.dataTables.min.js"></script>
    <script>window.jQuery.fn.DataTable || document.write('<script src="/static/djfrontend/js/jquery/jquery.dataTables/1.9.4/jquery.dataTables.min.js"><\/script>')</script>

djfrontend_jquery_datatables_css
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns the jQuery DataTables CSS file according to version number.
::

    <link rel="stylesheet" href="/static/djfrontend/css/jquery/jquery.dataTables/1.9.4/jquery.dataTables.css">

djfrontend_jquery_formset
~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns the jQuery Dynamic Formset plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback.
::

    <script src="/static/djfrontend/js/jquery/jquery.formset/1.2/jquery.formset.js"></script>

Or

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery.formset/1.2/jquery.formset.min.js"></script>
    <script>window.jQuery.fn.formset || document.write('<script src="/static/djfrontend/js/jquery/jquery.formset/1.2/jquery.formset.min.js"><\/script>')</script>

djfrontend_jquery_scrollto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns the jQuery ScrollTo plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback.
::

    <script src="/static/djfrontend/js/jquery/jquery.scrollTo/1.4.6/jquery.scrollTo.js"></script>

Or

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-scrollTo/1.4.6/jquery.scrollTo.min.js"></script>
    <script>window.jQuery.fn.scrollTo || document.write('<script src="/static/djfrontend/js/jquery/jquery.scrollTo/1.4.6/jquery.scrollTo.min.js"><\/script>')</script>

djfrontend_jquery_smoothscroll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Not a direct part of django-frontend-skeleton but can be used inside one of the included template blocks if static files are added.**

Returns the jQuery Smooth Scroll plugin JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from cdnjs with local fallback.
::

    <script src="/static/djfrontend/js/jquery/jquery.smooth-scroll/1.4.12/jquery.smooth-scroll.js"></script>

Or

::

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-smooth-scroll/1.4.12/jquery.smooth-scroll.min.js"></script>
    <script>window.jQuery.fn.smoothScroll || document.write('<script src="/static/djfrontend/js/jquery/jquery.smooth-scroll/1.4.12/jquery.smooth-scroll.min.js"><\/script>')</script>

djfrontend_twbs_css
~~~~~~~~~~~~~~~~~~~~
Returns Twitter Bootstrap CSS file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file. The latest '3.0.0' is included.
::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.0.0/bootstrap.css">

Or

::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.0.0/bootstrap.min.css">

djfrontend_twbs_theme_css
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns Twitter Bootstrap Theme CSS file according to version number.
::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.0.0/bootstrap-theme.css">

Or

::

    <link rel="stylesheet" href="/static/djfrontend/css/twbs/3.0.0/bootstrap-theme.min.css">

djfrontend_twbs_js
~~~~~~~~~~~~~~~~~~~~
Returns Twitter Bootstrap (3.0.0) JavaScript file(s). all returns concatenated file; full file for TEMPLATE_DEBUG, minified otherwise. Other choices include:

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

Individual files are not minified.

{% boostrap_js all %} would render
::

    <script src="/static/djfrontend/js/twbs/3.0.0/bootstrap.js"></script>

Or

::

    <script src="/static/djfrontend/js/twbs/3.0.0/bootstrap.min.js"></script>

{% bootstrap_js alert affix %} would render
::

    <script src="/static/djfrontend/js/twbs/3.0.0/bootstrap-affix.js"></script>
    <script src="/static/djfrontend/js/twbs/3.0.0/bootstrap-alert.js"></script>

Shout out to Ryan Brady and his `Django Bootstrapped <https://github.com/rbrady/django-bootstrapped>`_ for inspiration and initial code.

djfrontend_ga
~~~~~~~~~~~~~~
Returns Google Analytics asynchronous snippet if TEMPLATE_DEBUG is not set. Use DJFRONTEND_GA_SETDOMAINNAME to set domain for multiple, or cross-domain tracking. Set DJFRONTEND_GA_SETALLOWLINKER to use _setAllowLinker method on target site for cross-domain tracking.
::

    <script>var _gaq=[["_setAccount","UA-XXXXX-X"],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src="//www.google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>'

Or

::

    <script>var _gaq=[["_setAccount","UA-XXXXX-X"],["_setDomainName","%s"],["_setAllowLinker", true],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src="//www.google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>

Or

::

    <script>var _gaq=[["_setAccount","UA-XXXXX-X"],["_setDomainName","%s"],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src="//www.google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>

djfrontend_ios_fix
~~~~~~~~~~~~~~~~~~~~
Returns the iOS-Orientationchange-Fix.
::

    <script>/*! A fix for the iOS orientationchange zoom bug. Script by @scottjehl, rebound by @wilto.MIT / GPLv2 License.*/(function(a){function m(){d.setAttribute("content",g),h=!0}function n(){d.setAttribute("content",f),h=!1}function o(b){l=b.accelerationIncludingGravity,i=Math.abs(l.x),j=Math.abs(l.y),k=Math.abs(l.z),(!a.orientation||a.orientation===180)&&(i>7||(k>6&&j<8||k<8&&j>6)&&i>5)?h&&n():h||m()}var b=navigator.userAgent;if(!(/iPhone|iPad|iPod/.test(navigator.platform)&&/OS [1-5]_[0-9_]* like Mac OS X/i.test(b)&&b.indexOf("AppleWebKit")>-1))return;var c=a.document;if(!c.querySelector)return;var d=c.querySelector("meta[name=viewport]"),e=d&&d.getAttribute("content"),f=e+",maximum-scale=1",g=e+",maximum-scale=10",h=!0,i,j,k,l;if(!d)return;a.addEventListener("orientationchange",m,!1),a.addEventListener("devicemotion",o,!1)})(this);</script>