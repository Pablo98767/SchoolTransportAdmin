from email.headerregistry import Group
import random
import string
from django.db import models
from django.contrib.auth.models import User

# Motoristas
class Motorista(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    cnh_numero = models.CharField(max_length=20, unique=True)
    cnh_categoria = models.CharField(max_length=2, choices=[('A', 'A'), ('B', 'B'), ('D', 'D'), ('E', 'E')])
    cnh_validade = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.cnh_categoria}"

# Veículos
class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    capacidade = models.IntegerField()
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

# Rotas
class Rota(models.Model):
    nome = models.CharField(max_length=255)
    origem = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    horario_saida = models.TimeField()
    horario_chegada = models.TimeField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome} ({self.origem} ➝ {self.destino})"
    
    
# Alunos

class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    escola = models.CharField(max_length=255)
    endereco = models.TextField()
    responsavel = models.CharField(max_length=255)
    contato_responsavel = models.CharField(max_length=15)
    rota = models.ForeignKey('gestao.Rota', on_delete=models.CASCADE)

    PRESENCA_CHOICES = [
        ('vai_volta', 'Vai e volta'),
        ('so_vai', 'Só vai'),
        ('so_volta', 'Só volta'),
        ('nao_vai', 'Não vai e não volta'),
    ]
    
    presenca = models.CharField(max_length=20, choices=PRESENCA_CHOICES, default='vai_volta')
    data_presenca = models.DateField(null=True, blank=True)  

    def __str__(self):
        return self.nome
      