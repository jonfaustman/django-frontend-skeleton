# Django Frontend Skeleton

A basic Django template skeleton built on HTML5 Boilerplate and Twitter Bootstrap.

## Starring
* [HTML5 Boilerplate](https://github.com/h5bp/html5-boilerplate)
    * [Modernizr](https://github.com/Modernizr/Modernizr)
* [Twitter Bootstrap](https://github.com/twitter/bootstrap)
* [jQuery](https://github.com/jquery/jquery)
* [iOS-Orientationchange-Fix](https://github.com/scottjehl/iOS-Orientationchange-Fix)

## Getting Started

### Install
Add `git+ssh://git@github.com/jonfaustman/django-front-end-skeleton.git@feature/streamline` to your requirements file.

Add `frontend.skeleton` to your installed apps.

### Extend
Extend the HTML5 Boilerplate in your template(s) `{% extends 'h5bp.html' %}`

#### Template tags
Use the included template tags to suit your needs.

##### `{% load h5bp %}`

###### h5bp_html
Returns HTML tag according to chosen language - 'en' is the default.

``` HTML
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
```

###### h5bp_modernizr 
Returns Modernizr JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file. The latest '2.6.2' is the default and is included.

``` HTML
<script src="/static/js/h5bp/modernizr/2.6.2/modernizr.js"></script>
```

``` HTML
<script src="/static/js/h5bp/modernizr/2.6.2/modernizr.min.js"></script>
```

###### h5bp_jquery
Returns jQuery JavaScript file according to version number. TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback. The latest '1.8.2' is the default and is included.

``` HTML
<script src="/static/js/h5bp/jquery/1.8.2/jquery.js"></script>
```

``` HTML
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="/static/js/h5bp/jquery/1.8.2/jquery.min.js"><\/script>')</script>
```

`{% load bootstrap %}`

###### bootstrap_css
Returns Twitter Bootstrap CSS file. TEMPLATE_DEBUG returns full file, otherwise returns minified file.

``` HTML
<link rel="stylesheet" href="/static/css/bootstrap/bootstrap.css">
```

``` HTML
<link rel="stylesheet" href="/static/css/bootstrap/bootstrap.min.css">
```

###### bootstrap_responsive_css
Returns Twitter Bootstrap responsive CSS file. TEMPLATE_DEBUG returns full file, otherwise returns minified file.
``` HTML
<link rel="stylesheet" href="/static/css/bootstrap/bootstrap-responsive.css">
```

``` HTML
<link rel="stylesheet" href="/static/css/bootstrap/bootstrap-responsive.min.css">
```

###### bootstrap_js
Returns Twitter Bootstrap (2.1.1) JavaScript file(s). all returns concatenated file; full file for LOCAL, minified otherwise. Other choices include:
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

`{% boostrap_js all %}` would render
``` HTML
<script src="/static/js/bootstrap/bootstrap.js"></script>
```
or

``` HTML
<script src="/static/js/bootstrap/bootstrap.min.js"></script>
```

`{% bootstrap_js alert affix %}` would render
``` HTML
<script src="/static/js/bootstrap/bootstrap-affix.js"></script>
<script src="/static/js/bootstrap/bootstrap-alert.js"></script>
```

Shout out to Ryan Brady and his [Django Bootstrapped](https://github.com/rbrady/django-bootstrapped) for inspiration and initial code.

## License
MIT License

### Component Specific Licenses:
* HTML5 Boilerplate: MIT License
* Modernizr: BSD/MIT License
* Twitter Bootstrap: Apache License, Version 2.0
* jQuery: MIT/GPL License
* iOS-Orientationchange-Fix: MIT/GPL v2.0 License