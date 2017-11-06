from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Proforma(models.Model):
    """ La clase proformar guarada todos los datos de tipos de proformas que puede realizar el cliente """

    TIPO_PROFORMAS = (
        ('S','s_individuales'),
        ('R','r_servicios'),
        ('P','p_servicios'),
    )
    fecha = models.CharField(max_length=50)
    tipo_proformas = models.CharField(max_length=3, choices=TIPO_PROFORMAS)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
    	return "%s %s" %(self.id, self.fecha)
    	


