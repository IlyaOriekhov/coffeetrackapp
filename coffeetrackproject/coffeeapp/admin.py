from django.contrib import admin
from .models import Coffee, Recipe

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "roast_level", "process_method", "quantity", "owner")
    list_filter = ("country", "roast_level", "process_method")
    search_fields = ("name", "country", "owner__username")

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "method", "coffee", "owner")
    list_filter = ("method", "coffee")
    search_fields = ("title", "method", "coffee__name", "owner__username")

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Recipe)