from django.shortcuts import render
from Tienda.models import *
from django.http import HttpResponse
from django.template import loader
from Tienda.forms import *

# Create your views here.


#--------Navegacion-------------
'''
def first(request):
    return render(request, "FirstPage.html")

def out(request):
    return render(request, "FirstPage.html")
'''

def inicio(request):
    return render(request, "home.html")

def nosotros(request):
    return render(request, "nosotros.html")

def products(request):
    return render(request, "productos.html")

def proveedores(request):
    return render(request, "proveedores.html")

#----------PRODUCTOS--------------

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

def search_product(request):
    return render(request, "search_product.html")

def search(request):
    if request.GET["Producto"]:
        prd = request.GET["Producto"]
        productos = Productos.objects.filter(Prod_name__icontains = prd)
        
        return render(request, "search_result.html", {"productos":productos})

#----------Staff--------------

def ver_staff(request):
    staff = Staff.objects.all()
    dicc = {"staff": staff}
    print("contenido de productos")
    for name in staff:
        print(name.id, name.sname, name.slname, name.scateg, name.sstatus)
    print("contendio de dicc")
    print(dicc)
    plantilla = loader.get_template("nosotros.html")
    documento = plantilla.render(dicc)
    print("contenido de documento")
    print(documento)
    return HttpResponse(documento)

def new_staff(request):
    
    if request.method == "POST":
        
        formulario = Staff_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data

            staff = Staff(sname=datos["sname"], slname=datos["slname"], scateg=datos["scateg"], sstatus=datos["sstatus"])
            staff.save()
            print(datos)
            staff = Staff.objects.all()
            print("validado")
            
            return render(request, "nosotros.html", {"staff": staff})
        else:
            print("no validado", formulario.errors)
            
    return render(request, "Staff_form.html")

def eliminar_staff(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    
    staff = Staff.objects.all()
    return render(request, "nosotros.html", {"staff":staff})

def edit_staff(request,id):
    staff = Staff.objects.get(id=id)
    
    if request.method == "POST":
        formulario = Staff_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            staff.sname = datos["sname"]
            staff.slname = datos["slname"]
            staff.scateg= datos["scateg"]
            staff.sstatus= datos["sstatus"]
            staff.save()
            staff = Staff.objects.all()
            
            return render(request, "nosotros.html", {"staff":staff})
    
    else:
        formulario = Staff_formulario(initial={"sname": staff.sname, "slname":staff.slname, "scateg":staff.scateg, "sstatus":staff.sstatus})
    
    return render(request, "Staff_edit.html", {"formulario":formulario, "staff":staff})

def search_staff(request):
    return render(request, "search_staff.html")

def stsearch(request):
    if request.GET["Nombre"]:
        stf = request.GET["Nombre"]
        staff = Staff.objects.filter(sname__icontains = stf)
        
        return render(request, "stsearch_result.html", {"staff":staff})


#-----------Proveedores--------------

def ver_proveedores(request):
    proveedores = Proveedores.objects.all()
    dicc = {"proveedores":proveedores}
    print("contenido de productos")
    for proveedor in proveedores:
        print(proveedor.id, proveedor.RazonSocial, proveedor.NomFant, proveedor.Rut, proveedor.Giro)
    print("contendio dee dicc")
    print(dicc)
    plantilla = loader.get_template("proveedores.html")
    documento = plantilla.render(dicc)
    print("contenido dede documento")
    print(documento)
    return HttpResponse(documento)

def new_preveedor(request):
    
    if request.method == "POST":
        
        formulario = Proveedores_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data

            proveedores = Proveedores(RazonSocial=datos["RazonSocial"], NomFant=datos["NomFant"], Rut=datos["Rut"], Giro=datos["Giro"])
            proveedores.save()
            print(datos)
            proveedores = Proveedores.objects.all()
            print("validado")
            
            return render(request, "proveedores.html", {"proveedores": proveedores})
        else:
            print("no validado", formulario.errors)
            
    return render(request, "Prov_form.html")

def eliminar_proveedor(request, id):
    proveedores = Proveedores.objects.get(id=id)
    proveedores.delete()
    
    proveedores = Proveedores.objects.all()
    return render(request, "proveedores.html", {"proveedores":proveedores})

def edit_proveedor(request,id):
        proveedores = Proveedores.objects.get(id=id)
    
        if request.method == "POST":
            formulario = Proveedores_formulario(request.POST)
            if formulario.is_valid():
                datos = formulario.cleaned_data
                proveedores.RazonSocial = datos["RazonSocial"]
                proveedores.NomFant = datos["NomFant"]
                proveedores.Rut = datos["Rut"]
                proveedores.Giro = datos["Giro"]
                proveedores.save()
                proveedores = Proveedores.objects.all()
                
                return render(request, "proveedores.html", {"proveedores":proveedores})
        
        else:
            formulario = Proveedores_formulario(initial={"RazonSocial": proveedores.RazonSocial, "NomFant":proveedores.NomFant, "Rut":proveedores.Rut, "Giro":proveedores.Giro})
        
        return render(request, "Prov_edit.html", {"formulario":formulario, "proveedores":proveedores})

def search_proveedor(request):
    return render(request, "search_prov.html")

def provsearch(request):
    if request.GET["RazonSocial"]:
        pvd = request.GET["RazonSocial"]
        proveedores = Proveedores.objects.filter(RazonSocial__icontains = pvd)
        
        return render(request, "prvsearch_result.html", {"proveedores":proveedores})


'''

#---------Login--------------
    
def log_in(request):
    return render(request, "login.html")

def s_in(request):  
    email = request.GET["Email"]
    password = request.GET["Passw"]
    user = Registro(Email=email, Passw=password)
    if user is not None:
        return render(request, "home.html")
    else:
        return render(request, "register.html")


#--------Registro------------


def reg_user(request):
    if request.method == "POST":
        
        formulario = Registro_formulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data

            registro = Registro(fname=datos["fname"], lname=datos["lname"], Email=datos["Email"], Passw=datos["Passw"])
            registro.save()
            print(datos)
            registro = Registro.objects.all()
            print("validado")
            
            return render(request, "login.html", {"registro": registro})
        else:
            print("no validado", formulario.errors)
            
    return render(request, "register.html")


'def new_prod(request, Nombre, Costo, Venta):
    
    if request.method == "POST":
        nuevo = Productos(Prod_name=Nombre, Prod_cost=Costo, Prod_sale=Venta)
        nuevo.save()

        texto = f"Nuevo producto agregado {Productos.Prod_name} ${Productos.Prod_sale}"

        return render(request, "formulario.html", texto)
    
    return render(request, "formulario.html")
'''



