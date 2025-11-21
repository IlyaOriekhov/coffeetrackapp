from django.urls import path
from .views import (
    CoffeeListView, CoffeeCreateView, CoffeeDetailView,
    CoffeeUpdateView, CoffeeDeleteView, RecipeListView, RecipeCreateView, RecipeDetailView,
    RecipeUpdateView, RecipeDeleteView
)

urlpatterns = [
    path('coffees/', CoffeeListView.as_view(), name='coffee_list'),
    path('coffees/create/', CoffeeCreateView.as_view(), name='coffee_create'),
    path('coffees/<int:pk>/', CoffeeDetailView.as_view(), name='coffee_detail'),
    path('coffees/<int:pk>/edit/', CoffeeUpdateView.as_view(), name='coffee_edit'),
    path('coffees/<int:pk>/delete/', CoffeeDeleteView.as_view(), name='coffee_delete'),

    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/add/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),

]
