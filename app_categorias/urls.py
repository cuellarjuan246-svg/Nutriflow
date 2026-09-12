from django.http import HttpResponse
from django.urls import path

app_name = 'app_categorias'

urlpatterns = [
    path('', lambda request: HttpResponse("""
        <body style="font-family: Arial; text-align: center; background: #eeeeee;">
            <div style="background: white; width: 60%; margin: 100px auto; padding: 30px;">
                <h1 style="color: green;">Bienvenido a Categorías</h1>
                <p>Aquí se organizan las categorías de los productos.</p>
                <a href="/">Volver al inicio</a>
            </div>
        </body>
    """), name='bienvenido_categorias'),
]