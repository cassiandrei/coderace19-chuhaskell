from rest_framework.viewsets import ModelViewSet
from user.models import *
from .serializers import *


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = AvaliacaoSerializer


class GuiaViewSet(ModelViewSet):
    queryset = Guia.objects.all()
    serializer_class = AvaliacaoSerializer


class EspecidalidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = AvaliacaoSerializer
