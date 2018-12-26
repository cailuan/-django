from django import template
import datetime

register = template.Library()


@register.filter
def myLower(v):
    return v.lower()

@register.filter
def myjoin(v,n):
    return n.join(v)

@register.simple_tag
def mytime1(v):
    return datetime.datetime.now().strftime(v)

@register.simple_tag(takes_context=True)
def mytime2(context):
    return context.get('now')

@register.inclusion_tag('app_book/myclude.html')
def myclude(lis):
    return {'choices':lis}