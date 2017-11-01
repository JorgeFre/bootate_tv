from django.contrib import admin

from .models import Caracteristica, Servicio

	
@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
	'''
	    Admin View for Caracteristica
	'''
	# field_sets = [('Convocatoria'), {'fields': ['']}]
	list_display = ('id', 'servicio','descripcion')
	list_filter = ('servicio',)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
	'''
	    Admin View for Servicio
	'''
	# field_sets = [('Convocatoria'), {'fields': ['']}]
	list_display = ('id', 'nombre','tipo_servicios', 'valor')
	list_filter = ('nombre',)