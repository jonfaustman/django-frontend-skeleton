Template blocks
================
Use the included template blocks to suit your needs

html
-----
Override the HTML doctype, or use in conjunction with {% djfrontend_h5bp_html '' %} to change the HTML lang attribute.

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

djfrontend_h5bp_css
~~~~~~~~~~~~~~~~~~~~~
Block to include {% djfrontend_normalize '' %} and/or {% djfrontend_h5bp_css '' %}.

djfrontend_twbs_css
~~~~~~~~~~~~~~~~~~~~~
Block to override the included Twitter Bootstrap CSS and responsive CSS files.

head_js
---------
Override the included {% djfrontend_modernizr '2.6.2' %} or extend with JavaScript files that need to loaded in the head.

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

djfrontend_jquery
~~~~~~~~~~~~~~~~~~~
Override the included {% djfrontend_jquery '1.10.1' %} or use the included {% djfrontend_jquery '2.0.2' %}.

djfrontend_twbs_js
~~~~~~~~~~~~~~~~~~~~
Override the included {% djfrontend_twbs_js 'all' %}.

djfrontend_ga
~~~~~~~~~~~~~~~
Block to use {% h5bp_ga '' %} to include Google Analytics.

djfrontend_ios_fix
~~~~~~~~~~~~~~~~~~~~
Block to use {% djfrontend_ios_fix %} if iOS-Orientationchange-Fix is required. Deprecation warning: this block may be removed in future versions.