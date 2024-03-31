from django.db import models

# Create your models here.
class Registro(models.Model):
    
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30, null=True)
    Email = models.CharField(max_length=30)
    Passw = models.CharField(max_length=8)


class Productos(models.Model):
    
    Prod_name = models.CharField(max_length=50)
    Prod_cost = models.IntegerField()
    Prod_sale = models.IntegerField()
    
    def __str__(self):
        return f"{self.Prod_name} {self.Prod_cost} {self.Prod_sale}"

class Carrito(models.Model):
    
    Prod_Ncart = models.CharField(max_length=15)
    Prod_Scart = models.IntegerField()


class Staff(models.Model):
    
    sname = models.CharField(max_length=50)
    slname = models.CharField(max_length=50)
    scateg = models.CharField(max_length=50, null=True)
    sstatus = models.CharField(max_length=50)
    
    
