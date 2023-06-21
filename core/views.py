from rest_framework import viewsets
from .models import Usuario, Animal
from .serializer import UsuarioSerializer, AnimalSerializer
from rest_framework import fields, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

