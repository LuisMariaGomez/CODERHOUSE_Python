from django import forms

class CrearArco(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    potencia = forms.IntegerField()
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    tipo = forms.CharField(max_length=50)

class BuscarArcoForm(forms.Form):
    marca = forms.CharField(max_length=100, required=False)
    modelo = forms.CharField(max_length=100, required=False)
    tipo = forms.CharField(max_length=50, required=False)