from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='Home'),
    path("About/", views.ver_staff, name='About'),
    path("Productos/", views.ver_producto, name='Products'),
    path("login", views.log_in, name='Login'),
    path("Nuevo_Producto", views.new_prod, name="Nuevo"),
    path("Nuevo_Staff", views.new_staff, name="NStaff"),
    path("editar_producto/<int:id>", views.edit_prod, name="editar_producto"),
    path("editar_staff/<int:id>", views.edit_staff, name="edit_staff"),
    path("eliminar_producto/<int:id>", views.eliminar_producto, name="eliminar_producto"),
    path("eliminar_staff/<int:id>", views.eliminar_staff, name="el_staff"),
    path("buscar_producto", views.search_product, name="Buscar"),
    path("search", views.search),
    path("Registro", views.reg_user, name='regu'),
    path("sig_in", views.s_in, name='Log'),
    
]