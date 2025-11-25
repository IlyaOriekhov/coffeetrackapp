from django import forms
from .models import Coffee, Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ["name", "country", "roast_level", "process_method", "quantity", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control coffee-search-input"}),
            "country": forms.TextInput(attrs={"class": "form-control coffee-search-input"}),
            "roast_level": forms.TextInput(attrs={"class": "form-control coffee-search-input"}),
            "process_method": forms.TextInput(attrs={"class": "form-control coffee-search-input"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control coffee-search-input"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "method", "description", "ingredients", "instructions", "coffee", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control recipe-search-input"}),
            "method": forms.TextInput(attrs={"class": "form-control recipe-search-input"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "ingredients": forms.Textarea(attrs={"class": "form-control"}),
            "instructions": forms.Textarea(attrs={"class": "form-control"}),
            "coffee": forms.Select(attrs={"class": "form-select"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логін"})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"})
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логін"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"})
    )
    password2 = forms.CharField(
        label="Підтвердження пароля",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Підтвердження пароля"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]
