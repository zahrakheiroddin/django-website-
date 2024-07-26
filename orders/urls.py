from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('whcreate/', views.wh_order_create, name='wh_order_create'),
    path('admin/order/<int:order_id>/', views.admin_order_detail,name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),
    path('wh_admin/order/<int:order_id>/', views.wh_admin_order_detail,name='wh_admin_order_detail'),
    path('wh_admin/order/<int:order_id>/pdf/',views.wh_admin_order_pdf,name='wh_admin_order_pdf'),
    path('done/', views.done, name='done'),
]
