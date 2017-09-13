from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
	cedula = models.CharField(max_length = 13)
	nombres = models.CharField(max_length = 200)
	apellidos = models.CharField(max_length = 200)
	telefono = models.CharField(max_length = 9)
	celular = models.CharField(max_length = 14)
	direccion = models.CharField(max_length = 500)
	correo = models.CharField(max_length = 200)
	genero = models.CharField(max_length = 10)
	estado = models.BooleanField()
	image = models.FileField(null= True, blank=True)

	def __str__(self):
		return self.nombres


class Cliente(models.Model):
	cedula = models.CharField(max_length = 13)
	correo = models.CharField(max_length = 200)
	nombres = models.CharField(max_length = 200)
	apellidos = models.CharField(max_length = 200)
	telefono = models.CharField(max_length = 9)
	celular = models.CharField(max_length = 14)
	genero = models.CharField(max_length = 10)
	direccion = models.CharField(max_length = 500)

	def __str__(self):
		return self.nombres


