from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def h5bp_html(lang):
    """ Returns HTML tag according to chosen language.
    """
    output=[
        '<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="%s"> <![endif]-->' % lang,
        '<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="%s"> <![endif]-->' % lang,
        '<!--[if IE 8]>    <html class="no-js lt-ie9" lang="%s"> <![endif]-->' % lang,
        '<!--[if gt IE 8]><!--> <html class="no-js" lang="%s"> <!--<![endif]-->' % lang,
    ]
    return '\n'.join(output)


@register.simple_tag
def h5bp_normalize():
    """ Returns Normalize CSS file.
    """
    return '<link rel="stylesheet" href="%scss/h5bp/normalize.css">' % settings.STATIC_URL


@register.simple_tag
def h5bp_css():
    """ Returns HTML5 Boilerplate CSS file.
    """
    return '<link rel="stylesheet" href="%scss/h5bp/h5bp.css">' % settings.STATIC_URL


@register.simple_tag
def h5bp_modernizr(v):
    """ Returns Modernizr JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sjs/h5bp/modernizr/%s/modernizr.js"></script>' % (settings.STATIC_URL, v)
    else:
        return '<script src="%sjs/h5bp/modernizr/%s/modernizr.min.js"></script>' % (settings.STATIC_URL, v)


@register.simple_tag
def h5bp_jquery(v):
    """ Returns jQuery JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sjs/h5bp/jquery/%s/jquery.js"></script>' % (settings.STATIC_URL, v)
    else:
        output=[
            '<script src="//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"></script>' % v,
            '<script>window.jQuery || document.write(\'<script src="%sjs/h5bp/jquery/%s/jquery.min.js"><\/script>\')</script>' % (settings.STATIC_URL, v)
        ]
        return '\n'.join(output)


@register.simple_tag
def h5bp_ga(ua):
    """ Returns Google Analytics asynchronous snippet.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return ''
    else:
        return '<script>var _gaq=[["_setAccount","%s"],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src=("https:"==location.protocol?"//ssl":"//www")+".google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>' % ua