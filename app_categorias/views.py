from django.shortcuts import render


def inicio_categorias(request):
    return render(
        request,
        'app_categorias/categorias.html'
    )