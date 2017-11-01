from django.forms import ModelForm
from .models import Usuario
from django import forms

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ['C_I_persona', 'nombres', 'apellidos', 'celular', 'direccion', 'telefono', 'genero', 'fecha_ingreso', 'estado']