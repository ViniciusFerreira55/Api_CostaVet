from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    userFK = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, blank=False, null=False)
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

    def __str__(self):
        return self.nome_pet