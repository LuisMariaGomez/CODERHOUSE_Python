from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from usuarios.forms import FormularioRegistro

def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return render(request, 'inicio.html')
    else:
        formulario = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'formulario': formulario})

def registro_usuario(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('iniciar_sesion')
    else:
        formulario = FormularioRegistro()
    return render(request, 'registro_usuario.html', {'formulario': formulario})