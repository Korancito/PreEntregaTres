from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name='Home'),
    path("About/", views.nosotros, name='About'),
    path("Productos/", views.products, name='Products'),
    path("login/", views.login, name='Login'),
    path("Nuevo_Producto", views.new_prod, name="Nuevo"),
]

