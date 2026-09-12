from django.http import HttpResponse
from django.urls import path

app_name = 'app_inicio'

urlpatterns = [
    path('', lambda request: HttpResponse("""
        <body style="font-family: Arial; text-align: center; background: #eeeeee;">
            <div style="background: white; width: 60%; margin: 100px auto; padding: 30px;">
                <h1 style="color: green;">Bienvenido a NutriFlow</h1>
                <p>Sistema de gestión de suplementos nutricionales.</p>

                <a href="/app_productos/">Productos</a> |
                <a href="/app_inventario/">Inventario</a> |
                <a href="/app_clientes/">Clientes</a> |
                <a href="/app_ventas/">Ventas</a>
            </div>
        </body>
    """), name='bienvenido'),
]