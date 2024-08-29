from django.urls import path

from rest_framework.authtoken import views as auth_token

from .views import UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('api-token-auth/', auth_token.obtain_auth_token, name='create-token')
]
