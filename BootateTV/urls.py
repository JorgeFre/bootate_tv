from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'', include('home.urls',namespace="home")),
	url(r'^admin/', admin.site.urls),
    url(r'', include('ProductoraTV.urls')),
    url(r'^servicios/', include('servicios.urls', namespace='servicio')),
    url(r'^usuarios/', include('usuarios.urls', namespace='usuario')),
    url(r'^proformas/', include('proformas.urls', namespace='proforma')),
    url(r'^reservas/', include('reservas.urls', namespace='reserva')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls'))



]

if settings.DEBUG:
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)