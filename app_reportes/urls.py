from django.urls import path
from . import views


app_name = 'app_reportes'


urlpatterns = [
    path(
        '',
        views.inicio_reportes,
        name='bienvenido'
    ),
]