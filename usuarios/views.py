from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login
#from django.urls import reverse_lazy
from .models import Usuario
from .forms import UsuarioForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


class UsuarioCreate(CreateView):
    """ En esta clase presentamos una vista con campos oblifatorios para obtener los atributos de usuario """
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario:list')

    #fields = ['s_individuales']

class UsuarioUpdate(UpdateView):
    model = Usuario

class UsuarioDetail(DetailView):
    """ En esta clase presentamos los detalles de usuarios con campos inactivos de los atributos """
    model = Usuario 

class AuthorDelete(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario-list')

class UsuarioList(ListView):
    """ En esta clase de vistas de usuarios, listamos todas los detalles de un usuario """
    model = Usuario	

"""def autenticar(request):
	print (request.user)
	if not request.user.is_authenticated:
		print ("autenticando")

		if request.method=="POST":
			username = request.POST.get("username")
			password = request.POST.get("password")
			print ("autenticando")

			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("home:inicio")
			else:
				mensaje="usuario invalido"
				return render("usuarios/login.html", {"mensaje":mensaje})

	else:
		print("si esta logueado")
	return render(request, 'usuarios/login.html', {})
	"""


def autenticar(request):  
    response= HttpResponseRedirect(request.GET.get('next'))   
    if request.method == 'POST':
        print("AUTENTICANDO")
        username  = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            # return redirect("proformar:proformar")
            return response
        else:
            messages.error(request, 'Credenciales invalidas')
            return render(request, 'usuarios/login.html', {})

    else:
        print('usuario no autenticado')
        

        return render(request, 'usuarios/login.html', {})
                
    return render(request, 'usuarios:login', {})
