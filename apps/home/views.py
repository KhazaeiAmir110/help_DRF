from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404

from apps.core.permissions import IsOwnerOrReadOnly
from apps.home.models import Person, Questions
from apps.home.serializers import PersonSerializer, QuestionsSerializer


class HomeView(APIView):
    """
        View to render home page
    """

    def get(self, request):
        return Response({'message': 'Hello World!'})

    def post(self, request):
        data = request.data
        return Response(data)


class PersonView(APIView):
    """
        View to render person page
    """
    serializer_class = PersonSerializer

    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(instance=person, many=True)
        return Response(serializer.data)


# Use Of ApiView
class QuestionsView(APIView):
    """
        view to render questions page
    """
    serializer_class = QuestionsSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsOwnerOrReadOnly()]

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
        self.check_object_permissions(request, question)
        serializer = QuestionsSerializer(instance=question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Use Of ViewSer
class QuestionsViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    questions = Questions.objects.all()

    def list(self, request):
        serializer = QuestionsSerializer(instance=self.questions, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        question = get_object_or_404(self.questions, pk=pk)
        serializer = QuestionsSerializer(instance=question)
        return Response(data=serializer.data)

    def create(self, request):
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        question = get_object_or_404(self.questions, pk=pk)
        if request.user != question.user:
            return Response({'detail': 'You do not have permission !!!'}, status=status.HTTP_403_FORBIDDEN)
        serializer = QuestionsSerializer(instance=question, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        question = Questions.objects.get(pk=pk)
        if request.user != question.user:
            return Response({'detail': 'You do not have permission !!!'}, status=status.HTTP_403_FORBIDDEN)
        question.delete()
        return Response(data={'Success': 'Delete Question'}, status=status.HTTP_204_NO_CONTENT)
