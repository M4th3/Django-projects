from django.db import models



# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    idade = models.PositiveIntegerField(null=True, verbose_name='Idade')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    id = id
    def __str__(self):
        return f'Usuário: {self.nome}, idade: {self.idade}, CPF: {self.cpf}, id: {self.id}'

class Cargo(models.Model):
    cargo = models.CharField(max_length=100, verbose_name='Nome do cargo')
    funcao = models.CharField(max_length=200, verbose_name='Função do cargo')
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE, verbose_name='Usuário praticante')
    id = id
    def __str__(self):
        return f'Cargo: {self.cargo}, função: {self.funcao}, Usuário: {self.usuario}, id: {self.id}'
    
    