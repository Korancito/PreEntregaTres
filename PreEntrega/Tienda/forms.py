from django import forms

class Proveedores_formulario(forms.Form):
    
    RazonSocial = forms.CharField(max_length=30)
    NomFant = forms.CharField(max_length=30)
    Rut = forms.CharField(max_length=30)
    Giro = forms.CharField(max_length=30)
    

#---------------PRODUCTOS

class Productos_formulario(forms.Form):
    
    Prod_name = forms.CharField(max_length=50)
    Prod_cost = forms.IntegerField()
    Prod_sale = forms.IntegerField()
    
#----------------STAFF

class Staff_formulario(forms.Form):
    
    sname = forms.CharField(max_length=50)
    slname = forms.CharField(max_length=50)
    scateg = forms.CharField(max_length=50)
    sstatus = forms.CharField(max_length=50)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''class Carrito(forms.Form):
    
    Prod_Ncart = forms.CharField(max_length=15)
    Prod_Scart = forms.IntegerField()
'''