from ..models import Product,special,SpecialItem
from django import template
from django.shortcuts import render, get_object_or_404
register = template.Library()
from ..forms import Searchbox
@register.inclusion_tag('shop/product/discont_product.html')
def show_discont_posts():
    #speciall = special.objects.get(id=1)
    speciall= get_object_or_404(special, key='disc')
    item = SpecialItem.objects.filter(special = speciall)[:3]
    list=[]
    for i in item:
        list.append(i)
    return {'data': list}

@register.inclusion_tag('shop/product/sell_product.html')
def show_sell_posts():
    #speciall = special.objects.get(id=1)
    speciall= get_object_or_404(special, key='sell')
    item = SpecialItem.objects.filter(special = speciall)[:3]
    list=[]
    for i in item:
        list.append(i)
    return {'data': list}
@register.inclusion_tag('shop/product/search.html')
def show_search ():
    return{'searchform':Searchbox,}
