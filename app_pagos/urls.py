from django.urls import path
from . import views


app_name = 'app_pagos'


urlpatterns = [
    path(
        '',
        views.inicio_pagos,
        name='bienvenido'
    ),
]