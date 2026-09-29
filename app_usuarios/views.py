from django.shortcuts import render


def inicio_usuarios(request):
    return render(
        request,
        'app_usuarios/usuarios.html'
    )