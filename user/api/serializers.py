from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'nascimento', 'genero', 'telefone', 'image')


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('guia', 'turista', 'nota', 'comentario')


class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = ('nome',)


class CidadeSerializer(ModelSerializer):
    estado = EstadoSerializer()

    class Meta:
        model = Cidade
        fields = ('estado', 'nome', 'descricao', 'image')


class TipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('descricao',)


class EspecialidadeSerializer(ModelSerializer):
    tipo = TipoSerializer(many=True)

    class Meta:
        model = Especialidade
        fields = ('descricao', 'tipo')


class GuiaSerializer(ModelSerializer):
    especialidades = EspecialidadeSerializer(many=True)
    user = UserSerializer(required=True)

    class Meta:
        model = Guia
        fields = ('user', 'preco', 'especialidades')


class TuristaSerializer(ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Guia
        fields = ('user',)
