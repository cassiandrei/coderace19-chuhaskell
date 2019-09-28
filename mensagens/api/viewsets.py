from mensagens.models import Mensagem
from .serializers import MensagemSerializer
from rest_framework.viewsets import ModelViewSet

class MensagemViewSet(ModelViewSet):

    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer