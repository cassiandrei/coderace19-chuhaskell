from .serializers import *
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']


class UserEmailViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class GuiaViewSet(ModelViewSet):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer


class TuristaViewSet(ModelViewSet):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer


class EspecidalidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
