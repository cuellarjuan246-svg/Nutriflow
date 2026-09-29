from django.shortcuts import render


def inicio_pagos(request):
    return render(
        request,
        'app_pagos/pagos.html'
    )