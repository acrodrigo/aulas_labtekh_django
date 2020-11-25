from django.db import models
from apps.funcionario.models import Funcionario

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    data = models.DateField()
    horas_trabalhadas = models.DecimalField(max_digits=4, decimal_places=2)

    #def __str__(self):
    #    return self.funcionario.name, self.data