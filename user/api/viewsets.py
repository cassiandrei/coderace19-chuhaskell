from rest_framework.viewsets import ModelViewSet
from user.models import Avaliacao
from .serializers import RegistroSensorUmidadeSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = RegistroSensorUmidadeSerializer
