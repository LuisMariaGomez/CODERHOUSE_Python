from django.urls import path
from inicio.views import inicio, crear_arco, lista_arcos


urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear_arco/<marca>/<modelo>/<potencia>/<precio>/<tipo>/', crear_arco, name='crear_arco'),
    path('lista_arcos/', lista_arcos, name='lista_arcos'),
]