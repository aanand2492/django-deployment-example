# First step is to register your custom filter

from django import template

register = template.Library()

#@register.filter(name='cut1')
def cut1(value,arg):
    """
    This cuts out all the values of args from the string
    """
    return value.replace(arg,'')


register.filter('cut2',cut1)
