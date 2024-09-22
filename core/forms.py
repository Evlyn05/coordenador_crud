from django.forms import ModelForm
from django import forms
from .models import Coodenador

class CoodenadorForm(ModelForm):
    class Meta:
        model = Coodenador
        fields = '__all__'
      
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'Date'}),
            'matricula': forms.NumberInput(attrs={'class': 'form-control' }),
            'curso': forms.Select(attrs={'class': 'form-control' }),
        }