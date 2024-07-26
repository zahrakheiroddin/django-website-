from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem,wh_OrderItem
from .forms import OrderCreateForm,wh_OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
#**************
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order,wh_Order

#Rendering PDF files
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
#import weasyprint
from django.contrib.auth.decorators import login_required

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',{'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'css/pdf.css')])
    return response

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order': order})
@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_order=request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm(instance=request.user.profile)
        return render(request,'orders/order/create.html',{'cart': cart, 'form': form})
#**************************************
@staff_member_required
def wh_admin_order_detail(request, order_id):
    order = get_object_or_404(wh_Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order': order})

@staff_member_required
def wh_admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',{'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'css/pdf.css')])
    return response


@login_required
def wh_order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = wh_OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_order=request.user
            order.save()
            for item in cart:
                wh_OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('orders:done'))
    else:
        form = wh_OrderCreateForm(instance=request.user.profile)
        return render(request,'orders/order/whcreate.html',{'cart': cart, 'form': form})
def done(request):
    return render(request, 'orders/order/whcreated.html')
