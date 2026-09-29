from django.shortcuts import render


def inicio_reportes(request):
    return render(
        request,
        'app_reportes/reportes.html'
    )