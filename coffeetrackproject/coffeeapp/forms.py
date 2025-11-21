from django import forms
from .models import Coffee, Recipe

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ["name", "country", "roast_level", "process_method", "quantity"]

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "method", "description", "ingredients", "instructions", "coffee"]