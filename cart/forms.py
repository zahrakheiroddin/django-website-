from django import forms

class CartAddProductForm(forms.Form):
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    quantity=forms.IntegerField ( label=("تعداد"),widget=forms.TextInput(attrs={'class':'FnT', 'placeholder':"تعداد" }))
class wh_CartAddProductForm(forms.Form):

    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    quantity=forms.IntegerField ( label=("تعداد"),widget=forms.TextInput(attrs={'class':'FnT', 'placeholder':"تعداد" }))