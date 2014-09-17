from django.contrib import admin
from .models import Clientes, Productos, CategoriaProducto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','thumbnail','precio','stock')
    list_filter = ('nombre','precio')
    search_fields = ['nombre','precio']

    fields = ('nombre','descripcion',('precio','stock','imagen'),'categoria','status')


admin.site.register(Clientes)
admin.site.register(Productos,ProductoAdmin)
admin.site.register(CategoriaProducto)