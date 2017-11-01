from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def home(request):
	return render(request, 'index.html',{})

def quienes_somos(request):
	return render(request, 'about2.html',{})

def mostrar_servicios(request):
	return render(request,'services.html',{})

def realizar_proformas(request):
	servicios = Servicio.objects.all()
	return render(request,'services.html',{'servicios': servicios})	

def realizar_reservaciones(request):
	return render(request,'blog2.html',{})

def contactos(request):
	return render(request,'contact.html',{})

def reservar(request):
	return render(request,'reservas/reservar.html',{})