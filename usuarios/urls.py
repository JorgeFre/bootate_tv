from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
	url(r'^$', views.UsuarioList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.UsuarioDetail.as_view(), name='detail'),
	url(r'^new$', views.UsuarioCreate.as_view(), name='new'),
	url(r'^login/$', views.autenticar, name='login'),

]