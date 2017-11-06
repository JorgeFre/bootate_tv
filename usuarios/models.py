from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuario(models.Model):
    """ En esta clase presentamos los tipo de usuarios, estos pueden ser usuarios o clientes con sus atributos """
    TIPO_USUARIOS = (
        ('U','usuarios'),
        ('C','clientes'),
    )
    C_I_persona = models.CharField(max_length=10)
    tipo_usuarios = models.CharField(max_length=12, choices=TIPO_USUARIOS)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    celular = models.CharField(max_length=10)
    direccion = models.CharField(max_length=160)
    telefono = models.CharField(max_length=7)
    genero = models.CharField(max_length=10)
    fecha_ingreso = models.CharField(max_length=40)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" %(self.id, self.fecha)






