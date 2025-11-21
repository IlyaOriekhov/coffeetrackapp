from django import forms
from .models import Coffee, Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ["name", "country", "roast_level", "process_method", "quantity"]

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "method", "description", "ingredients", "instructions", "coffee"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']