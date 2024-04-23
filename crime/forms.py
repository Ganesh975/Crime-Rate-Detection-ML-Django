from django.contrib.auth.forms import UserCreationForm 
from django import forms
from . models import User

from .models import Search


class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Search
        fields = ['address', ]

class TForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ["uname","username","gender","phone_no","email"]