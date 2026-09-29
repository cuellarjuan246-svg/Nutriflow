from django.shortcuts import render


def inicio_productos(request):
    return render(
        request,
        'app_productos/productos.html'
    )