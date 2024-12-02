from django import forms
from .models import Temperatura

class TemperaturaForm(forms.ModelForm):
    class Meta:
        model = Temperatura
        fields = ['temperatura', 'data', 'hora']
        labels = {
            'temperatura': 'Temperatura',
            'data': 'Data',
            'hora': 'Hora'
        }
        widgets = {
            'temperatura': forms.NumberInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control'})
        }