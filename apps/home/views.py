from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ContactForm, LoginForm, RegisterForm
from apps.ventas.models import Productos
from django.core.mail import EmailMultiAlternatives #enviamos html
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from demo.settings import URL_LOGIN
import json

#paginacion
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.

def index_view(request):
    direc = ""
    if request.user.is_authenticated():
        direc = request.user
    ctx = {'dir':direc}
    return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def about_view(request):
    mensaje = "Somo una empresa reponsable contanctanos para mas informacion"
    ctx = {'msg':mensaje}
    return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))


def producto_view(request,pagina):
    if request.method == "POST":
        if "product_id" in request.POST:
            try:
                id_producto = request.POST['product_id']
                p = Productos.objects.get(pk=id_producto)
                mensaje = {"status":True,"product_id":p.id}
                p.delete()
                print("json 1: %s"%json.dumps(mensaje))
                return HttpResponse(json.dumps(mensaje),mimetype='application/json')
            except:
                mensaje = {'status':False}
                print("json 2: %s"%json.dumps(mensaje))
                return HttpResponse(json.dumps(mensaje),mimetype='application/json')


    lista_prod = Productos.objects.filter(status=True)
    paginator = Paginator(lista_prod,5) # 3= productos por pagina
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        productos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        productos = paginator.page(paginator.num_pages)
    ctx = {'productos':productos}
    return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
    info_enviado = False  #define si se envio la info o no
    email = ""
    titulo = ""
    texto = ""

    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data["Email"]
            titulo = formulario.cleaned_data["Titulo"]
            texto = formulario.cleaned_data["Texto"]

            #configuracion enviando mensaje via gmail

            to_admin = 'jc.fie.umich@gmail.com'
            html_content = "Informacion recivida  de: %s <br>El titulo es: %s<br>El contenido es: %s"%(email,titulo,texto)
            msg = EmailMultiAlternatives('correo de contacto',html_content,'from@server.com',[to_admin])
            msg.attach_alternative(html_content,'text/html') #definicio contenido como html
            msg.send()

    else:
        formulario = ContactForm()
    ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_inviado':info_enviado}
    return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect(next)
                else:
                    mensaje = "usuario y/o password incorectos/s"
        next = request.REQUEST.get('next')
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje,'next':next}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def singleProduct_view(request,id_prod):
    prod = Productos.objects.get(id=id_prod)
    cats = prod.categoria.all()#categorias de producto
    ctx = {'producto':prod,'categoria':cats}
    return render_to_response('home/singleProduct.html',ctx,context_instance=RequestContext(request))


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']

            u = User.objects.create(username=usuario,email=email,password=password_one)
            u.save()
            return render_to_response('home/graciasxregistrarte.html',context_instance=RequestContext(request))
    else:
        ctx = {'form':form}
        return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))