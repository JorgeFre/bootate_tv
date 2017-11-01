from django.shortcuts import render, render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#from django.urls import reverse_lazy
from .models import Servicio
from .forms import ServicioForm
from django.core.urlresolvers import reverse_lazy
from cart.cart import Cart


class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy('servicio:list')

    #fields = ['s_individuales']

class ServicioUpdate(UpdateView):
    model = Servicio

class ServicioDetail(DetailView):
    model = Servicio 

class AuthorDelete(DeleteView):
    model = Servicio
    success_url = reverse_lazy('servicio-list')

class ServicioList(ListView):
	model = Servicio		


def add_to_cart(request, servicio_id, quantity):
    servicio = Servicio.objects.get(id=servicio_id)
    cart = Cart(request)
    cart.add(servicio, servicio.valor, quantity)
    return render(request, 'proformas/proformar.html', { 'cart': cart })

def remove_from_cart(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)
    cart = Cart(request)
    cart.remove(servicio)
    return render(request, 'proformas/proformar.html', { 'cart': cart })
def get_cart(request):
    return render_to_response('proformas/proformar.html', dict(cart=Cart(request)))
# templates/cart.html

    # $(".qtyplus").click(function(){
    #     console.log("sumando item");
    #     var item_id=$(this).attr("item_id");
    #     console.log("item_id:"+item_id);
    #     var precio=$("#precio"+item_id).text();
    #     console.log("precio:"+precio);
    #     var cantidad=+$("#cant"+item_id).val()+1;
    #     $("#cant"+item_id).val(cantidad);
    #     console.log("cantidad: "+cantidad);
        
    #     var total= precio*cantidad;
    #     console.log ("total:"+total);

    #      $("#total"+item_id).text(total);
    #      calcular_total();

    # // });


    # // calculos de totales por item 
    #     $(".qtyminus").click(function(){
    #     var item_id= $(this).attr("item_id");
    #     console.log(item_id);
    #     var precio=$("#precio"+item_id).text();
    #     console.log("precio="+precio)

    #     var cantidad= $("#cant"+item_id).val()-1;
    #     console.log("cantidad"+ cantidad);
    #     $("#cant"+item_id).val(cantidad);

    #     var total= cantidad*precio;
    #     $("#total"+item_id).text(total);
    #     Calcular_totales();
    # });
    #  });