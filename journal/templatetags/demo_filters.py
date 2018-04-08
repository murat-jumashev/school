from django import template

register = template.Library()

@register.filter(name='remove_letter')
def remove_letter(value, arg):
    return value.replace(arg, '')

# register.filter('remove_letter', remove_letter)
