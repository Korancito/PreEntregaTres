from django.db import models

# Create your models here.
class Registro(models.Model):
    
    Usuario = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Passw = models.CharField(max_length=8)


class Productos(models.Model):
    
    Prod_name = models.CharField(max_length=15)
    Prod_cost = models.IntegerField()
    Prod_Sale = models.IntegerField()
    

class Carrito(models.Model):
    
    Prod_Ncart = models.CharField(max_length=15)
    Prod_SCart = models.IntegerField()
    