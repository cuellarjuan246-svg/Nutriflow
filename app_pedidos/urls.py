from django.http import HttpResponse
from django.urls import path

app_name = 'app_pedidos'

urlpatterns = [
    path('', lambda request: HttpResponse("""
        <body style="font-family: Arial; text-align: center; background: #eeeeee;">
            <div style="background: white; width: 60%; margin: 100px auto; padding: 30px;">
                <h1 style="color: green;">Bienvenido a Pedidos</h1>
                <p>Aquí se consultan los pedidos realizados.</p>
                <a href="/">Volver al inicio</a>
            </div>
        </body>
    """), name='bienvenido_pedidos'),
]