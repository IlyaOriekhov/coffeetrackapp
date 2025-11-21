from django.urls import path
from .views import (
    CoffeeListView, CoffeeCreateView, CoffeeDetailView,
    CoffeeUpdateView, CoffeeDeleteView
)

urlpatterns = [
    path('', CoffeeListView.as_view(), name='coffee_list'),
    path('create/', CoffeeCreateView.as_view(), name='coffee_create'),
    path('<int:pk>/', CoffeeDetailView.as_view(), name='coffee_detail'),
    path('<int:pk>/edit/', CoffeeUpdateView.as_view(), name='coffee_edit'),
    path('<int:pk>/delete/', CoffeeDeleteView.as_view(), name='coffee_delete'),

]
