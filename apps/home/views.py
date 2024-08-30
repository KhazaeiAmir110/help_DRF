from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person, Questions
from .serializers import PersonSerializer, QuestionsSerializer


class HomeView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'})

    def post(self, request):
        data = request.data
        return Response(data)


class PersonView(APIView):
    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(instance=person, many=True)
        return Response(serializer.data)


class QuestionsView(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]

    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(instance=questions, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Questions.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        question = Questions.objects.get(pk=pk)
        serializer = QuestionsSerializer(instance=question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
