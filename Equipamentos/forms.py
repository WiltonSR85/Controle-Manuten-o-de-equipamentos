from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):

    nome = forms.CharField(
        label='Nome do Equipamento',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do equipamento'
        })
    )

    modelo = forms.CharField(
        label='Modelo',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o modelo'
        })
    )

    numero_serie = forms.CharField(
        label='Número de Série',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o número de série'
        })
    )

    fabricante = forms.CharField(
        label='Fabricante',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do fabricante'
        })
    )

    data_aquisicao = forms.DateField(
        label='Data de Aquisição',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Selecione a data de aquisição'
        })
    )

    status = forms.ChoiceField(
        label='Status',
        choices=Equipamento.STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Equipamento
        fields = ['nome', 'modelo', 'numero_serie', 'fabricante', 'data_aquisicao', 'status']
