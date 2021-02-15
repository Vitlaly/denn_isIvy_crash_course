from django.forms import ModelForm
from .models import Order, Customer

# to next three imports for the registration user form

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('user',)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'    ------- it`s too same below
        fields = ['customer', 'product', 'status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


