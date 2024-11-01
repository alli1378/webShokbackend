from django import template
from ..models import Category
register=template.Library()
@register.simple_tag
def title():
    return 'وبلاگ  حجت'
@register.inclusion_tag('blog/partials/category_navbar.html')
def category_navbar():
    context_data={
        'category':Category.objects.filter(status=True)
    }
    return context_data
@register.inclusion_tag('registration/partials/link.html')
def link(request,link_name,content,icon):
    return{
        'request':request,
        'link_name':link_name,
        'content':content,
        'link':'account:{}'.format(link_name),
        'icon':icon
    }
