from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Arco

def inicio (request):
    return render(request, 'inicio.html')

def crear_arco(request, marca, modelo, potencia, precio, tipo):
    arco = Arco(marca=marca, modelo=modelo, potencia=potencia, precio=precio, tipo=tipo)
    arco.save()
    return render(request, 'crear_arco.html', {'arco_guardado' : arco})

def lista_arcos(request):
    arcos = Arco.objects.all()
    return render(request, 'lista_arcos.html', {'arcos': arcos})
