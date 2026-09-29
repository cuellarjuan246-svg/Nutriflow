from django.urls import path
from . import views


app_name = 'app_administrador'


urlpatterns = [
    path(
        '',
        views.inicio_administrador,
        name='bienvenido'
    ),
]