from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoReserva(models.Model):
    """ En esta clase presentamos el nombre y precio de los tipo de reservas """
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return "%s %s" %(self.id, self.nombre)



class Reserva(models.Model):
    """ En esta clase jalamos todos los atibutos de una reserva de los tipo de reservas """

    n_horas = models.IntegerField(default=0)
    dias = models.IntegerField(default=0)
    tipo_servicios = models.ForeignKey(TipoReserva, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=60)
    tipo_evento = models.CharField(max_length=60)
    fotografo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fotografo")
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cliente")
    fecha = models.DateField( )
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, blank=True, null=True)


    def __str__(self):
        return "%s %s" %(self.id, self.fecha)


class Agenda(models.Model):
    h_desde = models.TimeField()
    h_hasta = models.TimeField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return "%s %s" %(self.id, self.nombre)
