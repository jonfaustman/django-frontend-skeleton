Road Map
==============

0.8.0
------
* There will be wide-sweeping, non-backwards compatible changes - read carefully!
* The package will be renamed to djfrontend.djfrontend_skeleton. This will affect INSTALLED_APPS settings as well as the static location.
* The template tags will be combined into a single djfrontend_skeleton.py.
* {% load djfrontend_skeleton %} will load all template tags.
* 'bootstrap' will be renamed 'twbs' to reflect their branding change for 3.0.0.
* Every template tag will be namespaced with djfrontend\_. Full name changes are below:
* skeleton_ios_fix --> djfrontend_ios_fix
* h5bp_html --> djfrontend_html
* h5bp_normalize --> djfrontend_normalize
* h5bp_css --> djfrontend_h5bp_css
* h5bp_modernizr --> djfrontend_modernizr
* h5bp_jquery --> djfrontend_jquery
* h5bp_ga --> djfrontend_ga
* bootstrap_css --> djfrontend_twbs_css
* bootstrap_responsive_css --> djfrontend_twbs_responsive_css
* bootstrap_js --> djfrontend_twbs_js
* djfrontend_twbs_css, djfrontend_twbs_responsive_css and djfrontend_normalize will now require to be passed a version number.
* djfrontend_normalize, djfrontend_modernizr and djfrontend_jquery will be moved outside of h5bp to their own respective directories.
* All optional settings will be namespaced with djfrontend\_. Full name changes are below:
* SKELETON_STATIC_URL --> DJFRONTEND_STATIC_URL
* H5BP_GA_SETDOMAINNAME --> DJFRONTEND_GA_SETDOMAINNAME
* H5BP_GA_SETALLOWLINKER --> DJFRONTEND_GA_SETALLOWLINKER
* Template block names remain the same, although some are being considered for the chopping block.

1.0.0
-----
* Combine template tag libraries into skeleton. Tags will retain their name, but will require only one load.
* Use Git submodules for external libraries.
* Remove block ios_fix