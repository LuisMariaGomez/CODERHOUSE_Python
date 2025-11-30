from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Arco
from inicio.forms import CrearArco, BuscarArcoForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio (request):
    return render(request, 'inicio.html')

@login_required
def crear_arco(request):
    if request.method == 'POST':
        formulario = CrearArco(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            arco = Arco(
                marca=datos['marca'],
                modelo=datos['modelo'],
                potencia=datos['potencia'],
                precio=datos['precio'],
                tipo=datos['tipo'],
                imagen=datos['imagen'],
            )
            arco.save()
            return redirect('lista_arcos')
    else:
        formulario = CrearArco()
    return render(request, 'crear_arco.html', {'formulario': formulario})

def lista_arcos(request):
    formulario = BuscarArcoForm(request.GET)
    arcos = Arco.objects.all()
    if formulario.is_valid():
        info_a_buscar = formulario.cleaned_data
        if info_a_buscar.get('marca'):
            arcos = arcos.filter(marca__icontains=info_a_buscar['marca'])
        if info_a_buscar.get('modelo'):
            arcos = arcos.filter(modelo__icontains=info_a_buscar['modelo'])
        if info_a_buscar.get('tipo'):
            arcos = arcos.filter(tipo__icontains=info_a_buscar['tipo'])

    return render(request, 'lista_arcos.html', {'arcos': arcos, 'formulario': formulario})

def ver_arco(request, arco_id):
    arco = Arco.objects.get(id=arco_id)
    return render(request, 'ver_arco.html', {'arco': arco})

class EditarArco(LoginRequiredMixin, UpdateView):
    model = Arco
    template_name = 'editar_arco.html'
    success_url = reverse_lazy('lista_arcos')
    fields = '__all__'

class EliminarArco(LoginRequiredMixin, DeleteView):
    model = Arco
    template_name = 'eliminar_arco.html'
    success_url = reverse_lazy('lista_arcos')

def sobre_mi(request):
    return render(request, 'sobre_mi.html')