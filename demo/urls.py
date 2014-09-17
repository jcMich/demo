from django.conf.urls import patterns, include, url
from  demo import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^',include('apps.home.urls')),
    url(r'^',include('apps.ventas.urls')),
    url(r'^',include('apps.webServices.wsProductos.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
