from django.urls import path
from . import views


app_name = 'app_carrito'


urlpatterns = [
    path(
        '',
        views.inicio_carrito,
        name='bienvenido'
    ),
]