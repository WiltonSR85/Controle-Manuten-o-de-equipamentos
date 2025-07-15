from django import forms
from .models import OrdemManutencao
from Pecas.models import Peca
from .models import PecasManutencao

class OrdemManutencaoForm(forms.ModelForm):

    data_solicitacao = forms.DateField(
        label='Data da Solicitação',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Selecione a data da solicitação'
        })
    )

    tipo = forms.ChoiceField(
        label='Tipo',
        choices=OrdemManutencao.TIPO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    descricao_problema = forms.CharField(
        label='Descrição do Problema',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descreva o problema encontrado',
            'rows': 3
        })
    )

    status = forms.ChoiceField(
        label='Status',
        choices=OrdemManutencao.STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    equipamento = forms.ModelChoiceField(
        label='Equipamento',
        queryset=OrdemManutencao.equipamento.field.related_model.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })

    )

    tecnico_responsavel = forms.ModelChoiceField(
        label='Técnico Responsável',
        queryset=OrdemManutencao.tecnico_responsavel.field.related_model.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = OrdemManutencao
        fields = ['data_solicitacao', 'tipo', 'descricao_problema', 'status', 'equipamento', 'tecnico_responsavel']
        widgets = {
            'numero_ordem': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PecasManutencaoForm(forms.ModelForm):

    ordem_manutencao = forms.ModelChoiceField(
        queryset=PecasManutencao.ordem_manutencao.field.related_model.objects.all(),
        label="Ordem de Manutenção",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    peca = forms.ModelChoiceField(
        queryset=Peca.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = PecasManutencao
        fields = ['ordem_manutencao', 'peca']