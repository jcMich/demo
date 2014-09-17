from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import addProductoForm
from .models import Productos
from django.http import HttpResponseRedirect
# Create your views here.

def addProduct_view(request):
    info = "iniciaco"
    if request.method =="POST":
        form = addProductoForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.status = True
            add.save()  #guardamos la informacion
            form.save_m2m()  #guardar las relaciones many to many
            info = "Guardado satisfactoriamente"
            return HttpResponseRedirect('/producto/%s'%add.id)
    else:
        form = addProductoForm()
    ctx = {'form':form,'informacion':info}
    return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))

"""
def addProduct_view(request):
    info = "Inicializando"
    if request.user.is_authenticated():


        if request.method == "POST":
            form = addProductoForm(request.POST,request.FILES)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                descripcion = form.cleaned_data['descripcion']
                imagen = form.cleaned_data['imagen'] #Esto se obtienen con request.FILES
                precio = form.cleaned_data['precio']
                stock = form.cleaned_data['stock']

                p = Productos()
                if imagen:  #generar pequenia validacion
                    p.imagen = imagen
                p.nombre = nombre
                p.descripcion = descripcion
                p.status = True
                p.precio = precio
                p.stock = stock
                p.save()
                info = "Se guardo la informacion"


            else:
                info = "Informacion con datos erroneos"
            form = addProductoForm()
            ctx = {'form':form,'informacion':info}
            return render_to_response('ventas/addProducto.html',ctx, context_instance=RequestContext(request))

        else:
            form = addProductoForm()
            ctx = {'form':form}
            return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
"""
"""
def editProduct_view(request,id_prod):
    p = Productos.objects.get(id=id_prod)
    if request.method == "POST":
        form = addProductoForm(request.POST,request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            imagen = form.cleaned_data['imagen']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']

            p.nombre = nombre
            p.descripcion = descripcion
            p.precio = precio
            p.stock = stock
            if imagen:  #si existe nueva imagen
                p.imagen = imagen
            p.save()   #guardamos el modelo editado
            return HttpResponseRedirect('/producto/%s'%p.id)


    if request.method == "GET":
        form = addProductoForm(initial={
                                'nombre' : p.nombre,
                                'descripcion': p.descripcion,
                                'precio' : p.precio,
                                'stock': p.stock,
        })
    ctx = {'form':form,'producto':p}
    return render_to_response('ventas/editProducto.html',ctx,context_instance=RequestContext(request))
"""

def editProduct_view(request,id_prod):
    info = "Iniciado"
    prod = Productos.objects.get(id=id_prod)
    if request.method == "POST":
        form = addProductoForm(request.POST,request.FILES,instance=prod)
        if form.is_valid():
            edit_prod =  form.save(commit=False)
            form.save_m2m()
            edit_prod.status = True
            edit_prod.save()
            info = "Guardado satisfactoriamente"
            return HttpResponseRedirect('/producto/%s/'%edit_prod.id)
    else:
        form = addProductoForm(instance=prod)
    ctx = {'form':form,'informacion':info}
    return render_to_response('ventas/editProducto.html',ctx,context_instance=RequestContext(request))