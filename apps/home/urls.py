__author__ = 'root'
from  django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$','apps.home.views.index_view',name='index'),
    url(r'^about/$','apps.home.views.about_view',name='about'),
    url(r'^contacto/$','apps.home.views.contacto_view',name='contacto'),
    url(r'^productos/page/(?P<pagina>.*)/$','apps.home.views.producto_view',name='productos'),
    url(r'^producto/(?P<id_prod>.*)/$','apps.home.views.singleProduct_view',name='singleProducto'),
    url(r'^login/$','apps.home.views.login_view', name='login'),
    url(r'^logout/$','apps.home.views.logout_view', name='logout'),
    url(r'^registro/$','apps.home.views.register_view', name='register'),


)