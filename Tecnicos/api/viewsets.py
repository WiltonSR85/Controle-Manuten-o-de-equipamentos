from .serializers import TecnicoSerializer
from Tecnicos.models import Tecnico
from rest_framework import viewsets

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
