from django.urls import path
from inicio.views import inicio, crear_arco, lista_arcos, ver_arco, EditarArco, EliminarArco, sobre_mi


urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear_arco/', crear_arco, name='crear_arco'),
    path('lista_arcos/', lista_arcos, name='lista_arcos'),
    path('ver_arco/<int:arco_id>/', ver_arco, name='ver_arco'),
    path('editar_arco/<pk>/', EditarArco.as_view(), name='editar_arco'),
    path('eliminar_arco/<pk>/', EliminarArco.as_view(), name='eliminar_arco'),
    path('sobre_mi/', sobre_mi, name='sobre_mi'),
]