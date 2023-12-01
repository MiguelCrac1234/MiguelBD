from rest_framework import serializers, pagination

from .models import(
    countrylanguaje
)

class CountryLanguajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = countrylanguaje
        fields = ('__all__')
