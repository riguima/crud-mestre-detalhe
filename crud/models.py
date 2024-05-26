from django.db import models


class Company(models.Model):
    razao_social = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)


class Contact(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    observacao = models.CharField(max_length=100)
    recebe_email = models.BooleanField()
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
