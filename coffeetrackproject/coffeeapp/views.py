from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Coffee
from .forms import CoffeeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class CoffeeListView(LoginRequiredMixin, ListView):
    model = Coffee
    template_name = "coffee_list.html"
    context_object_name = "coffees"

    def get_queryset(self):
        return Coffee.objects.filter(user=self.request.user)

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

