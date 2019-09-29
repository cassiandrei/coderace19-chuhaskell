from rest_framework.serializers import ModelSerializer
from user.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('guia', 'turista', 'nota', 'comentario')


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('guia', 'turista', 'nota', 'comentario')


class GuiaSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('guia', 'turista', 'nota', 'comentario')