from django.shortcuts import render, get_object_or_404
from .models import Category, Product,Comment,Brand,Adv,special,SpecialItem
from cart.forms import CartAddProductForm
from .forms import CommentForm,Searchbox,opinion_form
import time
from blog.models import Post,DanPost
from cart.forms import wh_CartAddProductForm
# Create your views here.
def product_list(request,ti=None, category_slug=None):
    category = None
    productss = None
    categories = Category.objects.order_by('slug')
    brands= Brand.objects.order_by('slug')
    posts = Post.objects.order_by('-created')[:3]
    adv = Adv.objects.order_by('-created')[:3]
    brands = Brand.objects.all()
    if category_slug and ti == 'car' :
        products = Product.objects.filter(available=True).order_by('-number')

        category = get_object_or_404(Category, slug=category_slug)
        productss = products.filter(category=category)
        return render(request,'shop/product/mahsolat.html',{'products': productss,'category': category,'categories': categories,'Brands': brands})

    elif ti == 'brand':
        products = Product.objects.filter(available=True).order_by('-number')
        category = get_object_or_404(Brand, slug=category_slug)
        productss = products.filter(Brand=category)
        return render(request,'shop/product/mahsolat.html',{'products': productss,'category': category,'categories': categories,'Brands': brands})
    return render(request,'shop/product/list.html',{'products': productss,'category': category,'categories': categories,'Brands': brands,'adv':adv,'posts':posts,'opinion':opinion_form,})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    comments = product.comments.filter(active=True)
    cart_product_form = CartAddProductForm()
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
        # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'shop/product/detail.html',{'product': product, 'cart_product_form': cart_product_form, 'comment_form':CommentForm, 'comments':comments, 'new_comment': new_comment,'searchform':Searchbox})
def mahsol_list(request):
    brands = Product.objects.all()
    return render(request,'shop/product/mahsolat.html',{'products': brands,'searchform':Searchbox})
def About_us (request):
        return render(request,'shop/product/aboutus.html',{'searchform':Searchbox})
def contact_us (request):
    return render(request,'shop/product/contactus.html',{'searchform':Searchbox})
def searchwho_us (request):
    form = Searchbox(request.POST)
    if form.is_valid():
        text =form.cleaned_data['searchtxt']
        list = []
        products = Product.objects.all()
        for item in products:
            product_name = item.name
            if text in product_name:
                list.append(item)
    return render(request, 'shop/product/search_resultwh.html',{'prolist':list,'searchform':Searchbox,'cart_product_form':wh_CartAddProductForm})
def searchb_us (request):
    form = Searchbox(request.POST)
    if form.is_valid():
        text =form.cleaned_data['searchtxt']
        list = []
        products = Product.objects.all()
        for item in products:
            product_name = item.name
            if text in product_name:
                list.append(item)
    return render(request, 'shop/product/search_result.html',{'prolist':list,'searchform':Searchbox})
def pro_list (request, brand_slug=None):
    brand=None
    categories = Category.objects.order_by('slug')
    posts= Post.objects.order_by('-created')[:4]
    dan=DanPost.objects.order_by('-publish')[:4]
    if brand_slug:
        brand=get_object_or_404(Brand,slug=brand_slug)
        product=Product.objects.filter(Brand=brand)
    return render(request,'shop/product/listmahsolat.html',{'brand': brand, 'products':product,'categories': categories, 'posts':posts,'dan':dan,'searchform':Searchbox})
def opinion_views (request):
    form = opinion_form(request.POST)
    if form.is_valid():
        opinionp =opinion(
        name =form.cleaned_data['name'],
        email =form.cleaned_data['email'],
        title =form.cleaned_data['title'],
        body =form.cleaned_data['body'],
        )
        opinionp.save()
    return redirect('shop:secces')
def secces (request):
    return render(request,'shop/product/secces.html' )
def discount_views (request):
    speciall= get_object_or_404(special, key='disc')
    item = SpecialItem.objects.filter(special = speciall)
    list=[]
    for i in item:
        list.append(i)
    return render(request,'shop/product/special.html',{'products': list})

def bestsellers (request):
    speciall= get_object_or_404(special, key='sell')
    item = SpecialItem.objects.filter(special = speciall)
    list=[]
    for i in item:
        list.append(i)
    return render(request,'shop/product/special.html',{'products': list})
