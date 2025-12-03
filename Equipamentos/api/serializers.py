from rest_framework import serializers
from Equipamentos.models import Equipamento

class EquipamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = ['id', 'nome', 'modelo', 'numero_serie', 'fabricante', 'data_aquisicao','status']