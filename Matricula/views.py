from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CursoSerializer
from .models import Curso
# Create your views here.


class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.all() #select * from productos
    permission_classes=[permissions.AllowAny]
    serializer_class=CursoSerializer