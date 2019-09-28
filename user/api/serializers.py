from rest_framework.serializers import ModelSerializer
from user.models import Avaliacao


class RegistroSensorUmidadeSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'timestamp', 'valor')