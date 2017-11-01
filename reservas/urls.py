from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
	url(r'^$', views.ReservaList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.ReservaDetail.as_view(), name='detail'),
	url(r'^new$', views.ReservaCreate.as_view(), name='new'),
	url(r'^buscar$', views.reserva_buscar, name='buscar'),
	url(r'^reservar/(?P<tipo_reserva_id>\d+)$', views.reserva_reservar, name='reservar'),






]