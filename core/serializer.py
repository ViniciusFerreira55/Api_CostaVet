from rest_framework import serializers
from .models import Usuario, Animal
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'telefone', 'email', 'senha']

class AnimalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Animal
        fields = ['id', 'nome_pet', 'tipo_animal', 'idade_pet', 'sexo', 'dono']
