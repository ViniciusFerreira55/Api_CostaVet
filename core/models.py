from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    

class Animal(models.Model):
    nome_pet = models.CharField(max_length=50)
    tipo_animal = models.CharField(max_length=50)
    idade_pet = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    dono = models.ForeignKey(Usuario, on_delete=models.PROTECT)
