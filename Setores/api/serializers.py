from rest_framework import serializers
from Setores.models import Setor, EquipamentoSetor

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = 'id', 'nome', 'localizacao', 'tecnico_responsavel'

class EquipamentoSetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipamentoSetor
        fields = 'id', 'equipamento', 'setor'