from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm,wh_CartAddProductForm
from django.contrib.auth.decorators import login_required
from account.models import Profile
from shop.models import Product
from shop.forms import Searchbox
@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override'])
    return redirect('cart:cart_detail')
def cart_addh(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = wh_CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_h(product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override'])
    return redirect('cart:cart_detail_h')
@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})
def cart_detail_h(request):
    cart = Cart(request)
    userr =request.user
    data= userr.profile
    for item in cart:
        item['update_quantity_form'] = wh_CartAddProductForm(initial={'quantity': item['quantity'],'override': True})
    if data.check == True:
        product = Product.objects.all()
    return render(request, 'cart/detailh.html', {'cart': cart,'product':product, 'cart_product_form':wh_CartAddProductForm,'searchform':Searchbox})
