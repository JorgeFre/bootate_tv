from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
	url(r'^$', views.ProformaList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.ProformaDetail.as_view(), name='detail'),
	url(r'^new$', views.ProformaCreate.as_view(), name='new'),


]