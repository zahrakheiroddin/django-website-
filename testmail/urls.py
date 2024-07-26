from django.urls import path
from . import views
app_name = 'testmail'
urlpatterns = [

    path('',views.testing, name ='test'),
    path('contact',views.contactsendmail, name='contact'),



    ]
