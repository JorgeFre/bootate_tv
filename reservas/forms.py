from django.forms import ModelForm
from .models import Reserva
from django import forms

class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = ['n_horas', 'lugar', 'tipo_evento', 'fotografo', 'cliente', 'fecha']