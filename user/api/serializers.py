from rest_framework.serializers import ModelSerializer
from user.models import *


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('guia', 'turista', 'nota', 'comentario')


class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = ('estado', 'nome')


class GuiaSerializer(ModelSerializer):
    class Meta:
        model = Guia
        fields = ('user', 'preco', 'especialidades')


class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('descricao',)