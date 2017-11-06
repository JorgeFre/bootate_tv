from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
#from django.urls import reverse_lazy
from .models import Proforma
from .forms import ProformaForm
from django.core.urlresolvers import reverse_lazy


class ProformaCreate(CreateView):
	""" En esta clase de vistas de proforma, creamos una nueva proforma """
	model = Proforma
	form_class = ProformaForm
	success_url = reverse_lazy('proforma:list')

    #fields = ['s_individuales']

class ProformaUpdate(UpdateView):
	model = Proforma

class ProformaDetail(DetailView):
	""" En esta clase de vistas de proforma, presentamos todos los detalles de una nueva proforma """
	model = Proforma

class AuthorDelete(DeleteView):
	""" En esta clase de vistas de proforma, eliminamos todos los detalles de una nueva proforma """
	model = Proforma
	success_url = reverse_lazy('proforma-list')

class ProformaList(ListView):
	""" En esta clase de vistas de proforma, listamos todas los detalles de una nueva proforma """
	model = Proforma	