from django.urls import path
from . import views


app_name = 'app_clientes'


urlpatterns = [
    path(
        '',
        views.inicio_clientes,
        name='bienvenido'
    ),

    path(
        'registro/',
        views.registro_cliente,
        name='registro'
    ),
]