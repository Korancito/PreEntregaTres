from django.db import models


class Proveedores(models.Model):
    
    RazonSocial = models.CharField(max_length=30)
    NomFant = models.CharField(max_length=30, null=True)
    Rut = models.CharField(max_length=30)
    Giro = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.RazonSocial} {self.NomFant} {self.Rut} {self.Giro}"

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
    
    def __str__(self):
        return f"{self.sname} {self.slname} {self.scateg} {self.sstatus}"
    
    
