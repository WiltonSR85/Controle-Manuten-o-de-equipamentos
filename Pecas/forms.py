from django import forms
from .models import Peca

class PecaForm(forms.ModelForm):

    nome_da_peca = forms.CharField(
        label='Nome da Peça',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome da peça'
        })
    )

    codigo = forms.CharField(
        label='Código',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o código'
        })
    )

    fabricante = forms.CharField(
        label='Fabricante',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do fabricante'
        })
    )

    estoque = forms.IntegerField(
        label='Estoque',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a quantidade em estoque'
        })
    )

    data_da_ultima_compra = forms.DateField(
        label='Data da Última Compra',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Selecione a data da última compra'
        })
    )

    class Meta:
        model = Peca
        fields = ['nome_da_peca', 'codigo', 'fabricante', 'estoque', 'data_da_ultima_compra']
