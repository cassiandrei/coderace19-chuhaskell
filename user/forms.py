from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm, AuthenticationForm
from .models import User
from allauth.account.forms import SignupForm


# PLATAFORMA
class UserAuthenticate(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserAuthenticate, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


#novo
class UserCreate(SignupForm):
    first_name = forms.CharField(label='Nome', max_length=30)
    last_name = forms.CharField(label='Sobrenome', max_length=30)
    # phone = forms.CharField(label='Telefone Principal', max_length=20, required=True)

    # def save(self, request):
    #     # Save the provided password in hashed format
    #     user = super(UserCreate, self).save(request)
    #     user.phone = self.cleaned_data['phone']
    #     user.save()
    #     return user

    def clean_phone(self):
        return self.cleaned_data['phone'].replace(' ', '').replace('(', '').replace(')', '')

    def __init__(self, *args, **kwargs):
        super(UserCreate, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_superuser', 'is_active']

    def __init__(self, *args, **kwargs):
        super(UserUpdate, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class PasswordForm(AdminPasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


# ADMIN
class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'is_active', 'is_staff']

    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
