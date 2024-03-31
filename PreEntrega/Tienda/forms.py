from django import forms

class Registro_formulario(forms.Form):
    
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    Email = forms.CharField(max_length=30)
    Passw = forms.CharField(max_length=30)
    


class Productos_formulario(forms.Form):
    
    Prod_name = forms.CharField(max_length=50)
    Prod_cost = forms.IntegerField()
    Prod_sale = forms.IntegerField()
    
class Carrito(forms.Form):
    
    Prod_Ncart = forms.CharField(max_length=15)
    Prod_Scart = forms.IntegerField()
    

class Staff_formulario(forms.Form):
    
    sname = forms.CharField(max_length=50)
    slname = forms.CharField(max_length=50)
    scateg = forms.CharField(max_length=50)
    sstatus = forms.CharField(max_length=50)