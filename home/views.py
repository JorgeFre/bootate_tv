from django.shortcuts import render
from servicios.models import Servicio
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

def home(request):
	return render(request, 'index.html',{})

def quienes_somos(request):
	return render(request, 'about2.html',{})

def mostrar_servicios(request):
	return render(request,'services.html',{})

# @login_required()
def realizar_proformas(request):
	servicios = Servicio.objects.all()
	return render(request,'services.html',{'servicios': servicios})	

def realizar_reservaciones(request):
	return render(request,'blog2.html',{})

def contactos(request):
	return render(request,'contact.html',{})

def reservar(request):
	return render(request,'reservas/reservar.html',{})




def proformar(request):
	servicios = Servicio.objects.all()
	return render(request,'proformar.html',{'servicios': servicios})



def servicios(request):
	servicios = Servicio.objects.all()
	return render(request,'servicios.html',{'servicios': servicios})



def enviar_mail(request):
	sujeto = request.POST.get('subject')
	mensaje = request.POST.get('message')
	email_remitente = request.POST.get('email')
	send_mail( 
    	sujeto,
    	mensaje,
    	['jhtfilms76@hotmail.com', 'j19andres93@gmail.com',email_remitente],
    	fail_silendntly=False,
    	)
	messages.success(request, "email enviado correctamente")
	return render(request, 'contact.html',{'mensaje'})
