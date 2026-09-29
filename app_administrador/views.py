from django.shortcuts import render


def inicio_administrador(request):
    return render(request, 'app_administrador/administrador.html')