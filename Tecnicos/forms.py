from django import forms
from .models import Tecnico

class TecnicoForm(forms.ModelForm):

    nome = forms.CharField(
        label='Nome do Técnico',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do técnico'
        })
    )

    especialidade = forms.CharField(
        label='Especialidade',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a especialidade'
        })
    )

    contato = forms.CharField(
        label='Contato',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o contato'
        })
    )

    certificacoes = forms.CharField(
        label='Certificações',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite as certificações'
        })
    )

    class Meta:
        model = Tecnico
        fields = ['nome', 'especialidade', 'contato', 'certificacoes']

