from rest_framework import serializers
from Tecnicos.models import Tecnico

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = 'id', 'nome', 'especialidade', 'contato', 'certificacoes'