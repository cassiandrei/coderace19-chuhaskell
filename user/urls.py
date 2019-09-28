from django.conf.urls import url, include
from django.urls import path
from user import views

from mensagens.api.viewsets import MensagemViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'mensagem', MensagemViewSet)

app_name = 'user'
urlpatterns = [
    # include dos routers
    path('', include(router.urls)),
    # The home page
    path('<slug>/change', views.Profile.as_view(), name='profile'),
    path('password/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]
