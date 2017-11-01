from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#from django.urls import reverse_lazy
from .models import Proforma
from .forms import ProformaForm
from django.core.urlresolvers import reverse_lazy


class ProformaCreate(CreateView):
    model = Proforma
    form_class = ProformaForm
    success_url = reverse_lazy('proforma:list')

    #fields = ['s_individuales']

class ProformaUpdate(UpdateView):
    model = Proforma

class ProformaDetail(DetailView):
    model = Proforma

class AuthorDelete(DeleteView):
    model = Proforma
    success_url = reverse_lazy('proforma-list')

class ProformaList(ListView):
	model = Proforma	