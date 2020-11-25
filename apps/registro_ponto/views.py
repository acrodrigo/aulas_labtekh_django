from django.shortcuts import render
from .models import RegistroPonto


def ponto(request, id):
    ponto = RegistroPonto.objects.filter(funcionario__id__contains=id)
    print("Ponto ", ponto)
    return render(request, 'listar_ponto.html', {
        'registros': ponto
    })