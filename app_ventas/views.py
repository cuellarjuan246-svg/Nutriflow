from django.shortcuts import render


def inicio_ventas(request):
    return render(
        request,
        'app_ventas/ventas.html'
    )