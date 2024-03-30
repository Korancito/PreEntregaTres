from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='Home'),
    path("About/", views.nosotros, name='About'),
    path("Productos/", views.ver_producto, name='Products'),
    path("login/", views.login, name='Login'),
    path("Nuevo_Producto", views.new_prod, name="Nuevo"),
    path("editar_producto/<int:id>", views.edit_prod, name="editar_producto"),
    path("eliminar_producto/<int:id>", views.eliminar_producto, name="eliminar_producto" ),
    path("buscar_producto", views.search, name="Buscar")
    
]