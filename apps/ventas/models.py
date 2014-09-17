from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s"%(self.nombre, self.apellidos)


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=400)

    def __str__(self):
        return self.nombre




class Productos(models.Model):

    def url(self,filename):
        ruta = 'static/MultimediaData/Productos/%s/%s'%(self.nombre,str(filename))
        return ruta

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    status = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to=url,null=True,blank=True)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ManyToManyField(CategoriaProducto,null=True,blank=True)
    #para agregar campor sin eliminas db y seincronizar
    #mysql -u root -p
        #python manage.py sqlall ventas
    #mysql> use demo  (*)
    #mysql> alter table ventas_productos add (*) campo nuevo

    def __str__(self):
        return self.nombre


    def thumbnail(self):
        return '<a href="/%s"><img src="/%s" width="50px">'%(self.imagen,self.imagen)

    thumbnail.allow_tags = True
