from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def bootstrap_css():
    """ Returns Twitter Bootstrap CSS file.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<link rel="stylesheet" href="%sskeleton/css/bootstrap/bootstrap.css">' % settings.STATIC_URL
    else:
        return '<link rel="stylesheet" href="%sskeleton/css/bootstrap/bootstrap.min.css">' % settings.STATIC_URL


@register.simple_tag
def bootstrap_responsive_css():
    """ Returns Twitter Bootstrap responsive CSS file.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<link rel="stylesheet" href="%sskeleton/css/bootstrap/bootstrap-responsive.css">' % settings.STATIC_URL
    else:
        return '<link rel="stylesheet" href="%sskeleton/css/bootstrap/bootstrap-responsive.min.css">' % settings.STATIC_URL


@register.tag(name='bootstrap_js')
def do_bootstrap_js(parser, token):
    """ Returns Twitter Bootstrap (2.3.0) JavaScript file(s).
    all returns concatenated file; full file for TEMPLATE_DEBUG, minified otherwise.
    Other choice are:
        affix,
        alert,
        button,
        carousel,
        collapse,
        dropdown,
        modal,
        popover (adds tooltip if not included),
        scrollspy,
        tab,
        tooltip,
        transition,
        typeahead.
    Individual files are not minified.
    """
    return BootstrapJSNode(token.split_contents()[1:])


SCRIPT_TAG = '<script src="%sskeleton/js/bootstrap/bootstrap-%s.js"></script>'

class BootstrapJSNode(template.Node):

    def __init__(self, args):
        self.args = set(args)

    def render(self, context):
        if 'all' in self.args:
            if getattr(settings, 'TEMPLATE_DEBUG', ):
                return '<script src="%sskeleton/js/bootstrap/bootstrap.js"></script>' % settings.STATIC_URL
            else:
                return '<script src="%sskeleton/js/bootstrap/bootstrap.min.js"></script>' % settings.STATIC_URL
        else:
            # popover requires tooltip
            if 'popover' in self.args:
                self.args.add('tooltip')
            tags = [SCRIPT_TAG % (settings.STATIC_URL, tag) for tag in self.args]
            return '\n'.join(tags)