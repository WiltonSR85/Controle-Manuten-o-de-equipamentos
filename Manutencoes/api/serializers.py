from rest_framework import serializers
from Manutencoes.models import OrdemManutencao, PecasManutencao

class OrdemManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemManutencao
        fields = 'id', 'equipamento', 'data_solicitacao','tipo', 'descricao_problema', 'status', 'tecnico_responsavel'

class PecasManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PecasManutencao
        fields = 'id', 'ordem_manutencao', 'peca'