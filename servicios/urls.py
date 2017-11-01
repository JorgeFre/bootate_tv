from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
	url(r'^$', views.ServicioList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.ServicioDetail.as_view(), name='detail'),
	url(r'^new$', views.ServicioCreate.as_view(), name='new'),
	url(r'^remove_from_cart/(?P<servicio_id>\d+)$', views.remove_from_cart, name='remove_from_cart'),
	url(r'^get_cart$', views.get_cart, name='get_cart'),
	url(r'^add_to_cart/(?P<servicio_id>\d+)/(?P<quantity>\d+)$', views.add_to_cart, name='add_to_cart'),






]