from django.shortcuts import render
from django.http import HttpResponse
from apps.ventas.models import Productos
from django.core import serializers
# Create your views here.

def wsProductos_view(request):
    data = serializers.serialize("json",Productos.objects.filter(status=True))
    #retorna info en formato json
    return HttpResponse(data,mimetype='application/json')
