from django.urls import path
from . import views
app_name = 'payment'
urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('verify/', views.payment_verify, name='verify'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]
