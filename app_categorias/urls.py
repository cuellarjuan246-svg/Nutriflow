from django.urls import path
from . import views


app_name = 'app_categorias'


urlpatterns = [
    path(
        '',
        views.inicio_categorias,
        name='bienvenido'
    ),
]