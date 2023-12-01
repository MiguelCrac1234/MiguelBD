# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODEL
# ------------------------------------------------------------------

from .models import city

# ------------------------------------------------------------------
# FORMULARY
# ------------------------------------------------------------------
class NuevoCityForm(forms.ModelForm):
    """Form definition for Empleado."""
    class Meta:
        """Meta definition for Empleadoform."""
        # Modelo al que se aplica el formulario
        model = city
        # Campos usados en el formulario
        fields = (
            'NAME',
            'COUNTRYCODE',
            'DISTRICT',
        )
        # Labels de los campos del formulario
        labels = {
            'NAME': 'NAME',
            'COUNTRYCODE': 'COUNTRY CODE',
            'DISTRICT': 'DISTRICT',
        }
                # Espacio para agregar características a los campos
        widgets = {
            'DISTRICT': forms.CheckboxInput(
                attrs={'class': 'ContainerCityFormSelect'}
            ),
            'NAME': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'NAME'
                }
            ),
            'COUNTRYCODE': forms.TextInput(
                attrs={
                    'class': 'ContainerCountryCodeFormName',
                    'placeholder': 'Country Code'
                }
            ),
        }
