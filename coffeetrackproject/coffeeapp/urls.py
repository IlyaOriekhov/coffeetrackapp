from django.urls import path
from .views import (
    CoffeeListView, CoffeeCreateView, CoffeeDetailView,
    CoffeeUpdateView, CoffeeDeleteView, RecipeListView, RecipeCreateView, RecipeDetailView,
    RecipeUpdateView, RecipeDeleteView, login_view, register_view, logout_view
)

urlpatterns = [
    path('', CoffeeListView.as_view(), name='coffee_list'),
    path('create/', CoffeeCreateView.as_view(), name='coffee_create'),
    path('<int:pk>/', CoffeeDetailView.as_view(), name='coffee_detail'),
    path('<int:pk>/edit/', CoffeeUpdateView.as_view(), name='coffee_edit'),
    path('<int:pk>/delete/', CoffeeDeleteView.as_view(), name='coffee_delete'),

    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/add/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),


    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),

]
