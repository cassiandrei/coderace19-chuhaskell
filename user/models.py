from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext as _


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
    nascimento = models.DateField('Data de Nascimento')
    pais = models.CharField('País', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)

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


