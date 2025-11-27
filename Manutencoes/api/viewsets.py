from .serializers import OrdemManutencaoSerializer, PecasManutencaoSerializer
from Manutencoes.models import OrdemManutencao, PecasManutencao
from rest_framework import viewsets

class OrdemManutencaoViewSet(viewsets.ModelViewSet):
    queryset = OrdemManutencao.objects.all()
    serializer_class = OrdemManutencaoSerializer

class PecasManutencaoViewSet(viewsets.ModelViewSet):
    queryset = PecasManutencao.objects.all()
    serializer_class = PecasManutencaoSerializer