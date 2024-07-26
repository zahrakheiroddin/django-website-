from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [

    path('', views.cart_detail, name='cart_detail'),

    path('add/<int:product_id>/', views.cart_add, name='cart_add'),

    path('remove/<int:product_id>/', views.cart_remove,name='cart_remove'),
    path('h_cart/', views.cart_detail_h, name='cart_detail_h'),
    path('add_h/<int:product_id>/', views.cart_addh, name='cart_add_h'),
]
