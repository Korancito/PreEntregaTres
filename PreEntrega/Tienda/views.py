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

def registro(request):
    regi = Carrito.objects.all()
    pass


def registro(request):
    regi = Registro.objects.all()
    pass

'''def new_prod(request, Nombre, Costo, Venta):
    
    if request.method == "POST":
        nuevo = Productos(Prod_name=Nombre, Prod_cost=Costo, Prod_sale=Venta)
        nuevo.save()

        texto = f"Nuevo producto agregado {Productos.Prod_name} ${Productos.Prod_sale}"

        return render(request, "formulario.html", texto)
    
    return render(request, "formulario.html")
'''
def ver_producto(request):
    productos = Productos.objects.all()
    dicc = {"productos": productos}
    print("contenido de productos")
    for producto in productos:
        print(producto.id, producto.Prod_name, producto.Prod_cost, producto.Prod_sale)
    print("contendio dee dicc")
    print(dicc)
    plantilla = loader.get_template("productos.html")
    documento = plantilla.render(dicc)
    print("contenido dede documento")
    print(documento)
    return HttpResponse(documento)



def new_prod(request):
    
    if request.method == "POST":
        
        formulario = Productos_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data

            producto = Productos(Prod_name=datos["Prod_name"], Prod_cost=datos["Prod_cost"], Prod_sale=datos["Prod_sale"])
            producto.save()
            print(datos)
            producto = Productos.objects.all()
            print("producto validado")
            
            return render(request, "productos.html", {"productos": producto})
        else:
            print("producto no validado", formulario.errors)
            
            
    return render(request, "formulario.html")

def edit_prod(request,id):
    producto = Productos.objects.get(id=id)
    
    if request.method == "POST":
        formulario = Productos_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            producto.Prod_name = datos["Prod_name"]
            producto.Prod_cost = datos["Prod_cost"]
            producto.Prod_sale = datos["Prod_sale"]
            producto.save()
            producto = Productos.objects.all()
            
            return render(request, "productos.html", {"productos":producto})
    
    else:
        formulario = Productos_formulario(initial={"Prod_name": producto.Prod_name, "Prod_cost":producto.Prod_cost, "Prod_sale":producto.Prod_sale})
    
    return render(request, "editar_producto.html", {"formulario":formulario, "producto":producto})

def eliminar_producto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    
    producto = Productos.objects.all()
    return render(request, "productos.html", {"productos":producto})

def search(request):
    if request.GET["Prod_name"]:
        prd = request.GET["name"]
        producto = Productos.objects.filter(Prod_name__icontains = prd)
        
        return render(request, "resultado_busqueda.html", {"productos":producto})




def login(request):
    return render(request, "login.html")