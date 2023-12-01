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
    CitySerializer,
)

# ------------------------------------------------------------------
# API CREAT A CITY
# ------------------------------------------------------------------
class CityAPISerializer(CreateAPIView):
    serializer_class = CitySerializer
# ------------------------------------------------------------------
