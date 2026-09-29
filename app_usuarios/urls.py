from django.urls import path
from . import views


app_name = 'app_usuarios'


urlpatterns = [
    path(
        '',
        views.inicio_usuarios,
        name='bienvenido'
    ),
]