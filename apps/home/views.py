from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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
    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(instance=questions, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def delete(self, request, pk):
        pass

    def put(self, request, pk):
        pass
