from .serializers import *
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

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
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']


class GuiaViewSet(ModelViewSet):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__cidade__nome', 'especialidades__tipo__descricao', 'especialidades__descricao']


class TuristaViewSet(ModelViewSet):
    queryset = Turista.objects.all()
    serializer_class = TuristaSerializer


class EspecidalidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
