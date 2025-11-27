from rest_framework import serializers
from Pecas.models import Peca

class PecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peca
        fields = 'id', 'nome_da_peca', 'codigo', 'fabricante', 'estoque', 'data_da_ultima_compra'