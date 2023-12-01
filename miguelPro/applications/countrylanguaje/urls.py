from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "CountryLanguaje_app"

urlpatterns = [
        path('NewCountryLanguaje/',
                views.NuevoCOuntryLanguaje.as_view(),
                name='NewCOuntyLanguaje'),
        path('CountryLanguajeAPISerializer/',
                views.CountryLanguajeAPISerializer.as_view(),
                name='CountryLanguajeAPISerializer'),
]
