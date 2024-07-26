from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm,  ProfileEditForm,wholesaler
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#0033
from .models import Profile,wholesale_pass
from orders.models import Order
from shop.models import Product
from shop.forms import Searchbox
from cart.forms import wh_CartAddProductForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            nuser = authenticate(request,username=user_form.cleaned_data['username'],password=user_form.cleaned_data['password'])
            login(request, nuser)
            return redirect('account:edit')
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

@login_required
def dashboard(request):
    list = []
    userr =request.user
    user_Orders= userr.order.filter(paid=True)
    for i in user_Orders:
        order_item = i.items.filter()
        list.append(order_item)
    return render(request,'account/dashboard.html',{'section': 'dashboard', 'orders':user_Orders, 'item':lis,'searchform':Searchbox})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    userr =request.user
                    data= userr.profile
                    data.check = False
                    data.save()
                    return redirect('shop:product_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def logoutuser (request):
    if request.method == 'GET':
            logout(request)
            return redirect('shop:product_list')
#***************003
@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'profile_form': profile_form})
@login_required
def profile (request):
    userr =request.user
    data= userr.profile
    if data.check == True:
        form = None
        pro = Product.objects.all()
    else:
        form = wholesaler
        pro = None
    return render(request, 'account/profile.html', {'data':data, 'user':userr,'pass':form, 'product':pro,'cart_product_form':wh_CartAddProductForm,'searchform':Searchbox})
@login_required
def wholesale (request):

    form = wholesaler(request.POST)
    if form.is_valid():
        hpass =form.cleaned_data['hpass']
        passw = wholesale_pass.objects.all()
        list=[]
        for item in passw :
            passs = item.wpass
            list.append(passs)
        if hpass in list:
            prod = Product.objects.all()
            userr =request.user
            data= data= userr.profile
            data.check = True
            data.save()
            return render (request, 'account/wholesaler.html', {'test': 'لیست کالا', 'product':prod, 'cart_product_form':wh_CartAddProductForm,'data':data,'searchform':Searchbox})
    return render (request, 'account/wholesaler.html', {'test': 'کد وارد شده اشتباه است '})
