from django.forms import ModelForm
from .models import Servicio
from django import forms

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = ['nombre', 'tipo_servicios', 'valor']
