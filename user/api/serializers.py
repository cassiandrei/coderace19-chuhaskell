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


class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('descricao',)


class GuiaSerializer(ModelSerializer):
    especialidades = EspecialidadeSerializer(many=True)

    class Meta:
        model = Guia
        fields = ('user', 'preco', 'especialidades')
