import requests
from .models import *
from .serializer import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
import threading
import time


class UsuarioAPIView(APIView):
    def get(self, request, pk=''):
        if not pk:
            return Response({"msg": "without PK"})
        
        dados = Usuario.objects.get(userFK=pk)
        serializer = UsuarioSerializer(dados, many=True)
        return Response(serializer.data)


class AnimalAPIView(APIView):
    def get(self, request, pk=''):
        if not pk:
            return Response({"msg": "without PK"})
        
        dados = Animal.objects.all(dono=pk)
        serializer = AnimalSerializer(dados, many=True)
        return Response(serializer.data)