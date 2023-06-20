from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Animal
from .serializer import UsuarioSerializer, AnimalSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
