from django.urls import path
from . import views


app_name = 'app_vendedor'


urlpatterns = [
    path(
        '',
        views.inicio_vendedor,
        name='bienvenido'
    ),
]