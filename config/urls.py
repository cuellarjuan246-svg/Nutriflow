from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', include('app_inicio.urls')),

    # Módulos de NutriFlow
    path(
        'app_productos/',
        include('app_productos.urls')
    ),

    path(
        'app_categorias/',
        include('app_categorias.urls')
    ),

    path(
        'app_inventario/',
        include('app_inventario.urls')
    ),

    path(
        'app_clientes/',
        include('app_clientes.urls')
    ),

    path(
        'app_carrito/',
        include('app_carrito.urls')
    ),

    path(
        'app_ventas/',
        include('app_ventas.urls')
    ),

    path(
        'app_pagos/',
        include('app_pagos.urls')
    ),

    path(
        'app_promociones/',
        include('app_promociones.urls')
    ),

    path(
        'app_reportes/',
        include('app_reportes.urls')
    ),

    path(
        'app_usuarios/',
        include('app_usuarios.urls')
    ),
]