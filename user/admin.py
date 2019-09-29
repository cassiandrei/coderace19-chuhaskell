from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .forms import UserAdminCreationForm, UserAdminForm


# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('password', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('first_name', 'last_name', 'last_login', 'image')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'date_joined']
    ordering = ['first_name', 'last_name', 'date_joined']


admin.site.register(User, UserAdmin)
admin.site.register(Especialidade)
admin.site.register(Guia)
admin.site.register(Turista)
admin.site.register(Avaliacao)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)
