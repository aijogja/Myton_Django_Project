from django import forms
from tinymce.widgets import TinyMCE

class Send_email(forms.Form):
   email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'vTextField','readonly':'readonly'}))
   subject = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'vTextField'}))
   body = forms.CharField(required=True,widget=TinyMCE(attrs={'class': 'vTextField'}))
   
