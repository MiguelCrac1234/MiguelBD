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
    CountrySerializer,
)

# ------------------------------------------------------------------
# API CREAT A CITY
# ------------------------------------------------------------------
class CountryAPISerializer(CreateAPIView):
    serializer_class = CountrySerializer
# ------------------------------------------------------------------
