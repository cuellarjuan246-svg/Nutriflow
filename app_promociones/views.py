from django.shortcuts import render


def inicio_promociones(request):
    return render(
        request,
        'app_promociones/promociones.html'
    )