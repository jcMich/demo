__author__ = 'root'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^addProducto/$','apps.ventas.views.addProduct_view',name='addProducto'),
    url(r'^edit/producto/(?P<id_prod>.*)/$','apps.ventas.views.editProduct_view',name='editProducto'),
)