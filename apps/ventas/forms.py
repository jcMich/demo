__author__ = 'root'
from django import forms
from .models import Productos

class addProductoForm(forms.ModelForm):
    class Meta:
        model   = Productos
        exclude = {'status',}

"""
class addProductoForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.Textarea())
    imagen = forms.ImageField(required=False)
    precio = forms.DecimalField(required=True)
    stock = forms.IntegerField(required=True)




    def clean(self):
        return self.cleaned_data

"""