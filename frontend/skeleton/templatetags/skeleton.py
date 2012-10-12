from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def skeleton_html(lang):
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
def skeleton_modernizr(v):
    """ Returns Modernizr JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sskeleton/js/modernizr/%s/modernizr.js"></script>' % (settings.STATIC_URL, v)
    else:
        return '<script src="%sskeleton/js/modernizr/%s/modernizr.min.js"></script>' % (settings.STATIC_URL, v)


@register.simple_tag
def skeleton_jquery(v):
    """ Returns jQuery JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sskeleton/js/jquery/%s/jquery.js"></script>' % (settings.STATIC_URL, v)
    else:
        output=[
            '<script src="//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"></script>' % v,
            '<script>window.jQuery || document.write(\'<script src="%sskeleton/js/jquery/%s/jquery.min.js"><\/script>\')</script>' % (settings.STATIC_URL, v)
        ]
        return '\n'.join(output)