from django.db import models

# Create your models here.

from user.models import User

class Mensagem(models.Model):
    emissor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emissor')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    mensagem = models.TextField()
    time_stamp = models.DateField(auto_now_add=True)
