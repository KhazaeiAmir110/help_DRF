from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from .serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response(serializer.data)
        return Response(serializer.errors)
