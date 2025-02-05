from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext as _


class Pais(models.Model):
    nome = models.CharField('Nome', max_length=30)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=30)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=30)
    descricao = models.TextField('Descricao')
    image = models.ImageField('Foto de Perfil', upload_to='cidades',
                              null=True, blank=True)

    def __str__(self):
        return self.nome


# USER
class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=30)
    last_name = models.CharField(_('Last Name'), max_length=30)
    email = models.EmailField(_('Email Address'), max_length=255, unique=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)

    # NEW Fields
    image = models.ImageField('Foto de Perfil', upload_to='users', help_text='Selecione imagens para seu Perfil',
                              null=True, blank=True)
    nascimento = models.DateField('Data de Nascimento', default=timezone.now)
    # pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    # estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1)
    genero = models.CharField('Genero', max_length=6, default='male')
    telefone = models.CharField('Telefone', max_length=15, default='234325')

    USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['first_name', 'last_name']  # python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]


class Tipo(models.Model):
    SERVICOS = (('chat', 'Chat Online'),
                ('acompanhante', 'Acompanhante'))
    descricao = models.CharField('Descrição', max_length=10, choices=SERVICOS)

    def __str__(self):
        return self.descricao


class Especialidade(models.Model):
    descricao = models.CharField('Descrição', max_length=120)
    tipo = models.ManyToManyField(Tipo)

    def __str__(self):
        return self.descricao


class Guia(models.Model):
    especialidades = models.ManyToManyField(Especialidade)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preco = models.DecimalField('Preco', default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.first_name


# class Guia_Especialidade(models.Model):
#     SERVICOS = (('chat', 'Chat Online'),
#                 ('acompanhante', 'Acompanhante'))
#
#     guia = models.ForeignKey(Guia, on_delete=models.CASCADE)
#     especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
#     tipo = models.CharField('Tipo de Serviço', max_length=30, choices=SERVICOS)


class Turista(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Avaliacao(models.Model):
    guia = models.ForeignKey(Guia, models.CASCADE)
    turista = models.ForeignKey(Turista, models.CASCADE)
    nota = models.IntegerField('Nota de 1 a 5')
    comentario = models.TextField('Comentário')

    def __str__(self):
        return self.turista.user.first_name + ' em ' + self.guia.user.first_name
