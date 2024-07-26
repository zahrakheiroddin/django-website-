from .models import Comment,opinion
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
class Searchbox (forms.Form):
    searchtxt=forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'book-a-table-btn scrollto  d-lg-flex', 'placeholder':"جستجو در دوبيچو" }))
class opinion_form (forms.Form):
    name=forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"نام " }))
    email=forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"ايميل " }))
    title=forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"موضوع " }))
    body=forms.CharField (max_length=100, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':"متن " }))
