from django import template
register = template.Library()


@register.filter(name="split")
def split(value):
    split_path = value.split('/')
    return split_path[2]

@register.filter
def keys(value):
    keys = value.values()[0]
    key_list = []
    for key in keys:
        key_list.append(key)
    return key_list