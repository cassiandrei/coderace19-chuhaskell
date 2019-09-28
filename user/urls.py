from django.conf.urls import url
from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    # The home page
    path('<slug>/change', views.Profile.as_view(), name='profile'),
    path('password/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]
