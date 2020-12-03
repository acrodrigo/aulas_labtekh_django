from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_funcionarios, name='list_funcionario'),
    path('criar', views.criar_funcionario, name='create_funcionario'),
    path('editar/<int:id>', views.editar_funcionario, name='update_funcionario'),
    path('remover/<int:id>', views.deletar_usuario, name='delete_funcionario'),
    path('venda/<int:id>', views.vendas, name='vendas_funcionario')
]
