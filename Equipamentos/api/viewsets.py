from .serializers import EquipamentosSerializer
from Equipamentos.models import Equipamento
from rest_framework import viewsets

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentosSerializer