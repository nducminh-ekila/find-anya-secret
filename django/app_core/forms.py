from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
    
    password = forms.CharField(widget=forms.PasswordInput())

class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

