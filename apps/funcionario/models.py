from django.db import models


class Documento(models.Model):
    num_documento = models.CharField(max_length=20)

    def __str__(self):
        return self.num_documento

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    doc = models.OneToOneField(Documento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)


class Venda(models.Model):
    numero = models.IntegerField(primary_key=True)
    data = models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.PROTECT, null=True)
    produtos = models.ManyToManyField(Produto, blank=True)



