from django.shortcuts import render, HttpResponse, redirect
from .models import Funcionario, Venda
from .forms import FuncionarioForm


def home(request):
    return HttpResponse('Funcionario')


def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'listar_funcionarios.html', {'funcionario': funcionarios })


def criar_funcionario(request):
    form = FuncionarioForm(request.POST or None)


    if form.is_valid():
       form.save()
       return redirect('list_funcionario')

    return render(request, 'funcionario_form.html', {'form': form})


def editar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)

    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        return redirect('list_funcionario')

    return render(request, 'funcionario_form.html', {'form': form, 'funcionario': funcionario})


def deletar_usuario(request, id):
    funcionario = Funcionario.objects.get(id=id)

    if request.method == 'POST':
        funcionario.delete()
        return redirect('list_funcionario')

    return render(request, 'funcionario_confirm_delete.html', {'funcionario': funcionario})


def vendas(request, id):
    vendas = Venda.objects.filter(vendedor__id__contains=id)
    print('Vendas ', vendas)
    return render(request, 'vendas.html', {
        'vendas': vendas
    })