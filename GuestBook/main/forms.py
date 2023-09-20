from django import forms
from .models import *

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20 ,
                           widget=forms.TextInput(attrs={'class': 'form-control ' , 'placeholder':"name"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' :'form-control' , 'placeholder': 'enter your comment here '}))

    