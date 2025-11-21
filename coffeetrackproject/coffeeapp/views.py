from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Coffee, Recipe
from .forms import CoffeeForm, RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class CoffeeListView(LoginRequiredMixin, ListView):
    model = Coffee
    template_name = "coffee_list.html"
    context_object_name = "coffees"

    def get_queryset(self):
        return Coffee.objects.filter(owner=self.request.user)

class CoffeeCreateView(LoginRequiredMixin, CreateView):
    model = Coffee
    form_class = CoffeeForm
    template_name = "coffee_form.html"
    success_url = reverse_lazy("coffee_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CoffeeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Coffee
    template_name = "coffee_detail.html"

class CoffeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Coffee
    form_class = CoffeeForm
    template_name = "coffee_form.html"

    def get_queryset(self):
        return reverse_lazy('coffee_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        coffee = self.get_object()
        return coffee.owner == self.request.user

class CoffeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Coffee
    success_url = reverse_lazy('coffee_list')
    template_name = "coffee_confirm_delete.html"

    def test_func(self):
        coffee = self.get_object()
        return coffee.owner == self.request.user


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipe_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = reverse_lazy("recipe_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        recipe = self.get_object()
        return recipe.owner == self.request.user

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe_list")
    template_name = "recipe_confirm_delete.html"

    def test_func(self):
        recipe = self.get_object()
        return recipe.owner == self.request.user
