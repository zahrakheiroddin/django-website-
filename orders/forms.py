from django import forms
from .models import Order,wh_Order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','postal_code','phone', 'city']
class wh_OrderCreateForm(forms.ModelForm):
    class Meta:
        model = wh_Order
        fields = ['first_name', 'last_name', 'email', 'address','postal_code','phone', 'city']
