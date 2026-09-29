from django.urls import path
from . import views


app_name = 'app_ventas'


urlpatterns = [
    path(
        '',
        views.inicio_ventas,
        name='bienvenido'
    ),
]