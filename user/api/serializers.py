from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = User
        fields = ('email', 'password', 'nascimento', 'genero', 'telefone')
=======
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
>>>>>>> 39b83a56d065c50a8b6ae994426c3ba86bf2cef2
