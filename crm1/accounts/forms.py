from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

# This is another model like the models in models.py
class CustomerFrom(ModelForm):
    class Meta:
        model   = Customer
        fields  = '__all__'
        exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model   = Order
        fields  = '__all__' # These are the fields which will be shown in the front end form

class CreateUserForm(UserCreationForm):
    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']
        