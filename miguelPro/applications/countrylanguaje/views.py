from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

# ------------------------------------------------------------------
# APIS
# ------------------------------------------------------------------
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from .serializer import (
    CountryLanguajeSerializer,
)

# ------------------------------------------------------------------
# API CREAT A COUNTRYLANGUAJE
# ------------------------------------------------------------------
class CountryLanguajeAPISerializer(CreateAPIView):
    serializer_class = CountryLanguajeSerializer
# ------------------------------------------------------------------
