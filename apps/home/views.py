from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


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

