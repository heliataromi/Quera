from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    request = context['request']
    query = request.GET.copy()

    for key, value in kwargs.items():
        if value is None or value == 'none':
            query.pop(key, None)
        else:
            query[key] = value

    if query:
        return f"?{query.urlencode()}"
    return ''
