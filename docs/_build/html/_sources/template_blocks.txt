Template blocks
================
Use the included template blocks to suit your needs

Some blocks are specific to HTML5 Boilerplate or Twitter Bootstrap, while most are simply useful for template extension.

html
-----
Override the HTML doctype, or use in conjunction with {% h5bp_html '' %} to change the HTML lang attribute.

meta
-----
Override or extend meta tags and the title tag.

title
~~~~~~
Add your application specific title to the title tag.

meta_description
~~~~~~~~~~~~~~~~~~
Add your application specific information to the meta description.

head_css
----------
Parent CSS block to override or extend the included CSS files.

h5bp_css
~~~~~~~~~~
Block to include {% h5bp_normalize %} and/or {% h5bp_css %}.

bootstrap_css
~~~~~~~~~~~~~~~
Block to override the included Twitter Bootstrap CSS and responsive CSS files.

head_js
---------
Override the included {% h5bp_modernizr '2.6.2' %} or extend with JavaScript files that need to loaded in the head.

body_id
--------
Add an id to the body if needed.

body_class
------------
Add class(es) to the body if needed.

body_content
--------------
Override the Internet Explorer warning, and/or extend with the main content from your application.

body_js
---------
Override or extend the included JavaScript files with any file that does not need to be loaded in the head.

h5bp_jquery
~~~~~~~~~~~~
Override the included {% h5bp_jquery '1.9.1' %}.

bootstrap_js
~~~~~~~~~~~~~~
Override the included {% bootstrap_js 'all' %}.

h5bp_ga
~~~~~~~~
Block to use {% h5bp_ga '' %} to include Google Analytics.

ios_fix
~~~~~~~~
Block to use {% skeleton_ios_fix %} if iOS-Orientationchange-Fix is required. Deprecation warning: this block may be removed in future versions.