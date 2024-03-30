from django import forms

class Registro_formulario(forms.Form):
    
    Usuario = forms.CharField(max_length=30)
    Email = forms.CharField(max_length=30)


class Productos_formulario(forms.Form):
    
    Prod_name = forms.CharField(max_length=15)
    Prod_cost = forms.ImageField()
    Prod_sale = forms.IntegerField()
    
class Carrito(forms.Form):
    
    Prod_Ncart = forms.CharField(max_length=15)
    Prod_Scart = forms.IntegerField()