from django.shortcuts import render


def inicio_vendedor(request):
    return render(request, 'app_vendedor/vendedor.html')