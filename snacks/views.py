from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Snack


class SnackListView(ListView):
    template_name = 'index.html'
    model = Snack
    context_object_name = "snacks_list"


class SnackDetailView(DeleteView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'create_snack.html'
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackUpdateView(UpdateView):
    template_name = 'update_snack.html'
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackDeleteView(DeleteView):
    template_name = 'delete_snack.html'
    model = Snack
    success_url = '/'
