from django.shortcuts import render
from .models import Film
from .serializers import FilmSerializer
from rest_framework import viewsets


# Create your views here.
class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
