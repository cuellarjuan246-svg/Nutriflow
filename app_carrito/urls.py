from django.http import HttpResponse
from django.urls import path

app_name = 'app_carrito'

urlpatterns = [
    path('', lambda request: HttpResponse("""
        <body style="font-family: Arial; text-align: center; background: #eeeeee;">
            <div style="background: white; width: 60%; margin: 100px auto; padding: 30px;">
                <h1 style="color: green;">Bienvenido al Carrito</h1>
                <p>Aquí aparecen los productos seleccionados.</p>
                <a href="/">Volver al inicio</a>
            </div>
        </body>
    """), name='bienvenido_carrito'),
]