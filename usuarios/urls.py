from django.urls import path
from usuarios.views import iniciar_sesion, registro_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='cerrar_sesion.html'), name='cerrar_sesion'),
    path('registro_usuario/', registro_usuario, name='registro_usuario'),
]