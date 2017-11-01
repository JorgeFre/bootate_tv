from django.contrib import admin

from .models import Reserva, TipoReserva

	
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
	'''
	    Admin View for Reserva
	'''
	# field_sets = [('Convocatoria'), {'fields': ['']}]
	list_display = ('n_horas', 'tipo_servicios', 'lugar','tipo_evento','fotografo', 'cliente', 'fecha')
	list_filter = ('n_horas', 'tipo_servicios', 'lugar')


@admin.register (TipoReserva)
class TipoReservaAdmin(admin.ModelAdmin):
	'''
	    Admin View for TipoReserva
	'''
	# field_sets = [('Convocatoria'), {'fields': ['']}]
	list_display = ('id', 'nombre','precio')
	list_filter = ('nombre', 'precio')