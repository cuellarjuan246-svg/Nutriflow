from django.urls import path
from . import views


app_name = 'app_productos'


urlpatterns = [
    path(
        '',
        views.inicio_productos,
        name='bienvenido'
    ),
]