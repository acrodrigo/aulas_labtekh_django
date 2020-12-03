from django.contrib import admin
from .models import Funcionario, Documento, Venda, Produto

admin.site.register(Documento)
admin.site.register(Funcionario)
admin.site.register(Venda)
admin.site.register(Produto)