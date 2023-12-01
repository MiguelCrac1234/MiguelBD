from rest_framework import serializers, pagination

from .models import(
    city
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = ('__all__')
