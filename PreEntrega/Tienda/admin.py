from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Proveedores)
admin.site.register(Productos)
admin.site.register(Carrito)
admin.site.register(Staff)