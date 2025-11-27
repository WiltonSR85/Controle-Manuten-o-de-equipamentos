from .serializers import PecaSerializer
from Pecas.models import Peca
from rest_framework import viewsets

class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer
