from .serializers import SetorSerializer, EquipamentoSetorSerializer
from Setores.models import Setor, EquipamentoSetor
from rest_framework import viewsets

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class EquipamentoSetorViewSet(viewsets.ModelViewSet):
    queryset = EquipamentoSetor.objects.all()
    serializer_class = EquipamentoSetorSerializer