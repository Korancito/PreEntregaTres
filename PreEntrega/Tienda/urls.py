from django.urls import path
from . import views

urlpatterns = [
    
    #----------Navegacion----------
    path("", views.first, name='FirstPage'),
    path("Home/", views.inicio, name='Home'),
    path("About/", views.ver_staff, name='About'),
    path("Productos/", views.ver_producto, name='Products'),
    
    
    #---------Busqueda-------------
    
    path("buscar_producto", views.search_product, name="Buscar"),
    path("search", views.search),
    path("buscar_staff", views.search_staff, name="StBuscar"),
    path("stsearch", views.stsearch),
    
    
    #---------Creacion---------------
    
    path("Nuevo_Producto", views.new_prod, name="Nuevo"),
    path("Nuevo_Staff", views.new_staff, name="NStaff"),
    path("Registro", views.reg_user, name='regu'),

    #----------Edicion--------------

    path("editar_producto/<int:id>", views.edit_prod, name="editar_producto"),
    path("editar_staff/<int:id>", views.edit_staff, name="edit_staff"),   
    path("eliminar_producto/<int:id>", views.eliminar_producto, name="eliminar_producto"),
    path("eliminar_staff/<int:id>", views.eliminar_staff, name="el_staff"),    

    #-----------Login/out---------

    path("login", views.log_in, name='Login'),
    path("sig_in", views.s_in, name='Log'),
    path("log_out", views.out, name='out'),
    
    
]