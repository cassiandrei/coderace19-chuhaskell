"""coderaceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mensagens.api.viewsets import MensagemViewSet
from user.api.viewsets import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mensagem', MensagemViewSet)
router.register(r'user', UserViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'guias', GuiaViewSet)
router.register(r'especialidades', EspecidalidadeViewSet)

urlpatterns = [
    # include dos routers
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
