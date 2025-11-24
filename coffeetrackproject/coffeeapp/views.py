from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Coffee, Recipe
from .forms import CoffeeForm, RecipeForm, LoginForm, RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


class CoffeeListView(ListView):
    model = Coffee
    template_name = "coffee_list.html"
    context_object_name = "coffees"
    paginate_by = 10

    def get_queryset(self):
        queryset = Coffee.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)
        search_query = self.request.GET.get("search", "")
        country = self.request.GET.get("country", "")
        roast = self.request.GET.get("roast", "")
        price = self.request.GET.get("price", "")
        order_by = self.request.GET.get("order_by", "")

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        if country:
            queryset = queryset.filter(country=country)
        if roast:
            queryset = queryset.filter(roast_level=roast)
        if price:
            queryset = queryset.filter(price__lte=price)
        if order_by in ["price", "-price", "created", "-created"]:
            queryset = queryset.order_by(order_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["countries"] = Coffee.objects.values_list("country", flat=True).distinct()
        context["roasts"] = Coffee.objects.values_list("roast_level", flat=True).distinct()
        return context


class CoffeeCreateView(LoginRequiredMixin, CreateView):
    model = Coffee
    form_class = CoffeeForm
    template_name = "coffee_form.html"
    success_url = reverse_lazy("coffee_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CoffeeDetailView(DetailView):
    model = Coffee
    template_name = "coffee_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.filter(coffee=self.object)
        return context


class CoffeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Coffee
    form_class = CoffeeForm
    template_name = "coffee_form.html"

    def get_success_url(self):
        return reverse_lazy("coffee_detail", kwargs={"pk": self.get_object().pk})

    def test_func(self):
        coffee = self.get_object()
        return coffee.owner == self.request.user

    def get_queryset(self):
        return Coffee.objects.filter(owner=self.request.user)

class CoffeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Coffee
    success_url = reverse_lazy('coffee_list')
    template_name = "coffee_confirm_delete.html"

    def test_func(self):
        coffee = self.get_object()
        return coffee.owner == self.request.user


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 10

    def get_queryset(self):
        queryset = Recipe.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)
        search_query = self.request.GET.get("search", "")
        method = self.request.GET.get("method", "")
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        if method:
            queryset = queryset.filter(method=method)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["methods"] = Recipe.objects.values_list("method", flat=True).distinct()
        return context



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


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello {username}!")
                return redirect("coffee_list")
            else:
                messages.error(request, f"Incorrect username or password")
        return render(request, "login.html", {"form": form})

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("coffee_list")
        return render(request, "register.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect("coffee_list")

def home_view(request):
    return render(request, "home.html")
