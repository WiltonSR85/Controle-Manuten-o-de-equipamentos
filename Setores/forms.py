from django import forms
from .models import Setor
from Equipamentos.models import Equipamento
from Setores.models import EquipamentoSetor

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'responsavel', 'localizacao']

    nome = forms.CharField(
        label='Nome do Setor',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do setor'
        })
    )

    responsavel = forms.CharField(
        label='Responsavel pelo setor',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o responsável pelo setor'
        })
    )

    localizacao = forms.CharField(
        label='localização do setor',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a localização do setor'
        })
    )

class EquipamentoSetorForm(forms.ModelForm):
    equipamento = forms.ModelChoiceField(
        queryset=Equipamento.objects.all(),
        label="Equipamento",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    setor = forms.ModelChoiceField(
        queryset=Setor.objects.all(),
        label="Setor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = EquipamentoSetor
        fields = ['equipamento', 'setor']
