from django import template

register = template.Library()

@register.filter()
def precio_format(value):
    return '${0:.2f}'.format(value)