from django.contrib import admin
from .models import Usuario
from .models import Cliente

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class AdminUsuario(admin.ModelAdmin):
	list_display = ['cedula', 'nombres', 'apellidos', 'telefono', 'celular', 'direccion', 'correo', 'genero', 'estado', 'image']
	search_fields = ['nombres', 'apellidos', 'cedula']
	class Meta:
		model = Usuario
		

admin.site.register(Usuario, AdminUsuario)


class AdminCliente(admin.ModelAdmin):
	list_display = ['cedula', 'correo', 'nombres', 'apellidos', 'telefono', 'celular', 'genero', 'direccion']
	search_fields = ['nombres', 'apellidos', 'cedula']
	class Meta:
		model = Cliente


admin.site.register(Cliente, AdminCliente)