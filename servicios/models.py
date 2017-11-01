from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Servicio(models.Model):
    TIPO_SERVICIOS = (
        ('S_I','s_individuales'),
        ('R_S','r_servicios'),
        ('P_S','p_servicios'),
    )
    nombre = models.CharField(max_length=50)
    tipo_servicios = models.CharField(max_length=3, choices=TIPO_SERVICIOS)
    valor = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
    	return "%s %s" %(self.id, self.nombre)


class Caracteristica(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)


    def __str__(self):
        return "%s %s" %(self.id, self.servicio)