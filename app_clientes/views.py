from django.shortcuts import render


def inicio_clientes(request):
    return render(request, 'app_clientes/clientes.html')


def registro_cliente(request):
    return render(request, 'app_clientes/registro.html')