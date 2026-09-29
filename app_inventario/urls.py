from django.urls import path
from . import views


app_name = 'app_inventario'


urlpatterns = [
    path(
        '',
        views.inicio_inventario,
        name='bienvenido'
    ),
]