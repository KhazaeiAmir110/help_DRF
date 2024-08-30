from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from .serializers import UserRegisterSerializer, ListUserSerializer


class UserRegisterView(APIView):
    """
        view to register new user
    """
    serializer_class = UserRegisterSerializer
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


class ListUserView(APIView):
    """
        view to list users
    """
    serializer_class = ListUserSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = ListUserSerializer(instance=users, many=True)
        return Response(data=serializer.data)
