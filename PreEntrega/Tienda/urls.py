from django.urls import path
from . import views

urlpatterns = [
    
    #----------Navegacion----------
    #path("", views.first, name='Home'),
    path("", views.inicio, name='Home'),
    path("About/", views.ver_staff, name='About'),
    path("Productos/", views.ver_producto, name='Products'),
    path("proveedores/", views.ver_proveedores, name='Proveedores'),
    
    
    #---------Busqueda-------------
    
    path("buscar_producto", views.search_product, name="Buscar"),
    path("search", views.search),
    path("buscar_staff", views.search_staff, name="StBuscar"),
    path("stsearch", views.stsearch),
    path("buscar_prov", views.search_proveedor, name="PvBuscar"),
    path("provsearch", views.provsearch),
    
    
    #---------Creacion---------------
    
    path("Nuevo_Producto", views.new_prod, name="Nuevo"),
    path("Nuevo_Staff", views.new_staff, name="NStaff"),
    path("Nuevo_Prov", views.new_preveedor, name="NProv"),

    #----------Edicion--------------

    path("editar_producto/<int:id>", views.edit_prod, name="editar_producto"),
    path("editar_staff/<int:id>", views.edit_staff, name="edit_staff"),
    path("editar_prov/<int:id>", views.edit_proveedor, name="edit_prov"),      
    path("eliminar_producto/<int:id>", views.eliminar_producto, name="eliminar_producto"),
    path("eliminar_staff/<int:id>", views.eliminar_staff, name="el_staff"),  
    path("eliminar_prov/<int:id>", views.eliminar_proveedor, name="el_prov"),  

    #-----------Registro/Login/out---------

    #path("login", views.log_in, name='Login'),
    #path("sig_in", views.s_in, name='Log'),
    #path("log_out", views.out, name='out'),
    #path("Registro", views.reg_user, name='regu'),
    
]