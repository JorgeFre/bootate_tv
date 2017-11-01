from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta
#from django.urls import reverse_lazy
from .models import Reserva, TipoReserva
from .forms import ReservaForm
from django.core.urlresolvers import reverse_lazy




class ReservaCreate(CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy('reserva:list')

    #fields = ['s_individuales']

class ReservaUpdate(UpdateView):
    model = Reserva

class ReservaDetail(DetailView):
    model = Reserva 

class AuthorDelete(DeleteView):
    model = Reserva
    success_url = reverse_lazy('reserva-list')

class ReservaList(ListView):
	model = Reserva


def reserva_buscar(request):
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

def reserva_reservar(request,tipo_reserva_id):
	formato1 = " %Y-%m-%d"
	if request.method == "POST":
		f_desde = request.POST.get('fecha_desde')
		f_hasta = request.POST.get('fecha_hasta')

		fecha_desde = datetime.strptime(f_desde, formato1)
		fecha_hasta = datetime.strptime(f_hasta, formato1)

		n_dias = (fecha_desde - fecha_hasta)
		print ( n_dias )
		tipo_reserva_id = request.POST.get("tipo_reserva_id")
		tipo_reserva = TipoReserva.objects.get(id=tipo_reserva_id)
		fotografos = User.objects.filter(groups__name='Fotografos')
		precio_servicio = tipo_reserva.precio
		context = {
		'fotografos': fotografos, 'precio_servicio': precio_servicio
		}
		return render(request,'reservas/reservar.html', context)

	else: 
		tipo_reserva = TipoReserva.objects.get(id=tipo_reserva_id)
	context={
				'tipo_reserva': tipo_reserva, 

	}


	return render(request,'reservas/reserva_search.html', context)