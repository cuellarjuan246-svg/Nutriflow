from django.shortcuts import render


def inicio_carrito(request):
    return render(
        request,
        'app_carrito/carrito.html'
    )