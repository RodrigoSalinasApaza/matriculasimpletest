from django.urls import path,include
from rest_framework import routers
from .views import CursoViewSet

ruta=routers.DefaultRouter()
ruta.register('cursos',CursoViewSet)

urlpatterns=[
    path('',include(ruta.urls))
]