from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta
from django.contrib.auth.decorators import login_required
from decimal import Decimal
#from django.urls import reverse_lazy
from .models import Reserva, TipoReserva
from .forms import ReservaForm
from django.core.urlresolvers import reverse_lazy




class ReservaCreate(CreateView):
	""" En esta clase presentamos una vista con campos oblifatorios para obtener los atributos """
	model = Reserva
	form_class = ReservaForm
	success_url = reverse_lazy('reserva:list')

    #fields = ['s_individuales']

class ReservaUpdate(UpdateView):
	model = Reserva

class ReservaDetail(DetailView):
	""" En esta clase presentamos los detalles de resrva con campos inactivos de los atributos """
	model = Reserva 

class AuthorDelete(DeleteView):
	model = Reserva
	success_url = reverse_lazy('reserva-list')

class ReservaList(ListView):
	model = Reserva

@login_required()
def reserva_buscar(request):
	""" En clase una vez elegida el tipoo de reserva, se procede a elegir una fecha desde, hasta  """
	tipo_reservas = TipoReserva.objects.all()
	if request.method == "POST":
		f_desde = request.POST.get('fecha_desde')
		f_hasta = request.POST.get('fecha_hasta')
		tipo_reserva_id = request.POST.get("tipo_reserva")
		tipo_reserva = TipoReserva.objects.get(id=tipo_reserva_id)
		print(f_desde+f_hasta+tipo_reserva.nombre)

	else: 

		print(tipo_reservas)

	context={
		'tipo_reservas': tipo_reservas, 
	}
	
@login_required()
def reserva_reservar(request,tipo_reserva_id):
	""" Una vez seleccionada el tipo de reserva de fotgrafo, le da a elegir una fecha desde, hasta de la misma """
	date_format = "%Y-%m-%d"
	if request.method == "POST":


		f_desde = datetime.strptime(request.POST.get("fecha_desde"), date_format)
		f_hasta = datetime.strptime(request.POST.get("fecha_hasta"), date_format)
		delta = f_hasta - f_desde
		n_dias = delta.days
		print(delta.days) # that's it


		

		tipo_reserva_id = request.POST.get("tipo_reserva_id")
		tipo_reserva = TipoReserva.objects.get(id=tipo_reserva_id)
		fotografos = User.objects.filter(groups__name='Fotografos')
		precio_servicio = tipo_reserva.precio
		context = {
		'n_dias': n_dias,
		'fotografos': fotografos, 
		'precio_servicio': precio_servicio,
		'tipo_reserva': tipo_reserva,
		}
		return render(request,'reservas/reservar.html', context)

	else: 
		tipo_reserva = TipoReserva.objects.get(id=tipo_reserva_id)
	context={
				'tipo_reserva': tipo_reserva, 

	}


	return render(request,'reservas/reserva_search.html', context)


def reserva_guardar(request):
	""" Una vez llenados todos los campos obligatorios, se guarda y lista todos los atributos de la reserva """

	fotografo_id = request.POST.get("fotografo")
	fotografo= User.objects.get(id=fotografo_id)
	hora = request.POST.get("hora_hidden")
	dias = request.POST.get("dias")
	lugar = request.POST.get("lugar_hidden")
	precio = request.POST.get("precio")
	tipo_servicio = TipoReserva.objects.get(id=request.POST.get("tipo_servicio_id"))
	print(precio)
	reserva = Reserva(
		n_horas=hora,
		lugar=lugar,
		tipo_servicios=tipo_servicio,
		fotografo=fotografo,
		#precio=precio,
		dias=dias,
		cliente= request.user,
		fecha= date.today()
		) 
	reserva.save()
	reservas=Reserva.objects.filter(cliente=request.user)
	return render(request,'reservas/reserva_list.html', {'object_list':reservas})