from django.urls import path
from . import views


app_name = 'app_promociones'


urlpatterns = [
    path(
        '',
        views.inicio_promociones,
        name='bienvenido'
    ),
]