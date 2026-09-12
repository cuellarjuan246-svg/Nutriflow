from django.http import HttpResponse
from django.urls import path

app_name = 'app_usuarios'

urlpatterns = [
    path('', lambda request: HttpResponse("""
        <body style="font-family: Arial; text-align: center; background: #eeeeee;">
            <div style="background: white; width: 60%; margin: 100px auto; padding: 30px;">
                <h1 style="color: green;">Bienvenido a Usuarios</h1>
                <p>Aquí se administran los usuarios y sus roles.</p>
                <a href="/">Volver al inicio</a>
            </div>
        </body>
    """), name='bienvenido_usuarios'),
]