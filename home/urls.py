from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.home, name='inicio'),
	url(r'^quienes_somos/$',views.quienes_somos, name='quienes_somos'),
	url(r'^mostrar_servicios/$',views.mostrar_servicios, name='mostrar_servicios'),


	url(r'^proformar/$',views.proformar, name='proformar'),


	url(r'^servicios/$',views.servicios, name='servicios'),
	url(r'^realizar_proformas/$',views.realizar_proformas, name='realizar_proformas'),
	url(r'^realizar_reservaciones/$',views.realizar_reservaciones, name='realizar_reservaciones'),
	url(r'^contactos/$',views.contactos, name='contactos'),
	url(r'^reservar/$',views.reservar, name='reservar'),
	url(r'^enviar_mail/$',views.enviar_mail, name='enviar_mail'),




	#url(r'^servicios/$',views.servicios, name='servicios')
   # url(r'^login/$', views.mostrar_login),#
   
   
    

]