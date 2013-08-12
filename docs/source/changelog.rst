Changelog
==============

1.1.0
------
* jQuery updated to v1.10.2 and v2.0.3
* jQuery smooth-scroll updated to v.1.4.11
* Twitter Bootstrap (TWBS) updated to v3.0.0 RC1
* TWBS typeahead, glyphicons and bootstrap-responsive removed per TWBS v3.0.0 RC1

1.0.0
------
* There was wide-sweeping, non-backwards compatible changes - read carefully!
* Packaged renamed to djfrontend. This will affect INSTALLED_APPS settings as well as the static location.
* 'skeleton/base.html' is now 'djfrontend/skeleton.html'.
* Template tags combined into a single djfrontend.py.
* {% load djfrontend %} loads all template tags.
* 'bootstrap' renamed 'twbs' to reflect their branding change for 3.0.0.
* djfrontend_normalize, djfrontend_modernizr and djfrontend_jquery moved outside of h5bp to their own respective directories.
* djfrontend_twbs_css, djfrontend_twbs_responsive_css and djfrontend_normalize now require to be passed a version number.
* Every template tag namespaced with djfrontend\_. Full name changes are below:
* skeleton_ios_fix --> djfrontend_ios_fix
* h5bp_html --> djfrontend_h5bp_html
* h5bp_css --> djfrontend_h5bp_css
* h5bp_normalize --> djfrontend_normalize
* h5bp_modernizr --> djfrontend_modernizr
* h5bp_jquery --> djfrontend_jquery
* h5bp_ga --> djfrontend_ga
* bootstrap_css --> djfrontend_twbs_css
* bootstrap_responsive_css --> djfrontend_twbs_responsive_css
* bootstrap_js --> djfrontend_twbs_js
* All optional settings namespaced with djfrontend\_. Full name changes are below:
* SKELETON_STATIC_URL --> DJFRONTEND_STATIC_URL
* H5BP_GA_SETDOMAINNAME --> DJFRONTEND_GA_SETDOMAINNAME
* H5BP_GA_SETALLOWLINKER --> DJFRONTEND_GA_SETALLOWLINKER
* Some template are now namespaced with djfrontend\_. Full name changes are below:
* h5bp_css --> djfrontend_h5bp_css
* bootstrap_css --> djfrontend_twbs_css
* h5bp_jquery --> djfrontend_jquery
* bootstrap_js --> djfrontend_twbs_js
* h5bp_ga --> djfrontend_ga
* ios_fix --> djfrontend_ios_fix

0.7.2
------
* Update to jQuery 1.10.1 and 2.0.2 (HTML5 Boilerplate)
* Update docs to include SKELETON_STATIC_URL.
* Include individual licenses.

0.7.1
------
* Update to Twitter Bootstrap 2.3.2 (Twitter Bootstrap)

0.7.0
-----
* Added jQuery 2.0.0 (HTML5 Boilerplate)
* Added SKELETON_STATIC_URL for optional dedicated static server/CDN setting
* Added Road Map

0.6.0
-----
* Remove Google Analytics protocol check (HTML5 Boilerplate)
* Update Normalize.css to 1.1.1 (HTML5 Boilerplate)
* Update to Twitter Bootstrap 2.3.1 (Twitter Bootstrap)
* Added H5BP_GA_SETDOMAINNAME and H5BP_GA_SETALLOWLINKER for optional Google Analytics customization (HTML5 Boilerplate)
* iOS-Orientationchange-Fix moved out of base.html
* iOS-Orientationchange-Fix now {% skeleton_ios_fix %}
* Created 'skeleton' template tag library

0.5.0
------
* Update to jQuery 1.9.1 (HTML5 Boilerplate)
* Update to Twitter Bootstrap 2.3.0 (Twitter Bootstrap)

0.4.0
------
* Update to jQuery 1.9.0 (HTML5 Boilerplate)
* Update to Normalize.css 1.1.0 (HTML5 Boilerplate)
* Update h5bp.css (HTML5 Boilerplate)
* Include changelog

0.3.0
------
* Namespace static files under 'skeleton'
* Remove trailing slash from MANIFEST.in
* Documentation update/improvement

0.2.0
------
* Update to Twitter Bootstrap 2.2.2 (Twitter Bootstrap)
* Fix Glyphicons URL (Twitter Boostrap)
* Add documentation
* Minimize Readme

0.1.0
------
* Initial release