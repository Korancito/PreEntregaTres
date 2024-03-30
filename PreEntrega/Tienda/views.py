from django.shortcuts import render
from Tienda.models import Registro
from Tienda.models import Carrito
from Tienda.models import Productos
from django.http import HttpResponse
from django.template import loader
from Tienda.forms import *

# Create your views here.


def inicio(request):
    return render(request, "home.html")

def nosotros(request):
    return render(request, "nosotros.html")


def products(request):
    return render(request, "productos.html")


'''def new_prod(request, Nombre, Costo, Venta):
    
    if request.method == "POST":
        nuevo = Productos(Prod_name=Nombre, Prod_cost=Costo, Prod_sale=Venta)
        nuevo.save()

        texto = f"Nuevo producto agregado {Productos.Prod_name} ${Productos.Prod_sale}"

        return render(request, "formulario.html", texto)
    
    return render(request, "formulario.html")
'''


def new_prod(request):
    
    if request.method == "POST":
        
        formulario = Productos_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.claned_data

            producto = Productos(Prod_name=datos["Nombre"], Prod_cost=datos["Costo"], Prod_sale=datos["Venta"])
            producto.save()
            return render(request, "formulario.html")
    
    return render(request, "formulario.html")



def login(request):
    return render(request, "login.html")