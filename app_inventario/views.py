from django.shortcuts import render


def inicio_inventario(request):
    return render(
        request,
        'app_inventario/inventario.html'
    )