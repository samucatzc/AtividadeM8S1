
from django.db import models


class Categoria(models.Model):
     tipo = models.CharField(max_length=150)
     tamanho = models.CharField(max_length=150)
     def __str__(self):
          return f'Tamanho {self.tamanho}, {self.tipo}'

class Pet(models.Model):
     nome = models.CharField(max_length=150)
     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Agendamento(models.Model):
     nome = models.CharField(max_length=150)
     email = models.EmailField()
     nome_do_pet = models.CharField(max_length=150)
     data = models.DateField()
     observacoes = models.TextField(blank=True, null=True)
     def __str__(self):
          return f'Agendamento criado {self.nome}, {self.email}, {self.nome_do_pet}, {self.data}'


class Contato(models.Model):
     nome = models.CharField(max_length=150)
     email = models.EmailField()
     mensagem = models.TextField()
     def __str__(self):
          return f'Contato criado {self.nome}, {self.email}'

class Reserva(models.Model):
     nome_do_pet = models.CharField(max_length=150)
     telefone = models.CharField(max_length=15)
     data = models.DateField()
     mensagem = models.TextField(blank=True, null=True)
     def __str__(self):
          return f'Reserva criada {self.nome_do_pet}, {self.data}'
