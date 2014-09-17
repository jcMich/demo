from django.conf.urls import patterns, url

urlpatterns = patterns('apps.webServices.wsProductos.views',
    url(r'^ws/productos/$','wsProductos_view',name='wsProductos'),
)