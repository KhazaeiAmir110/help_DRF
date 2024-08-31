from django.urls import path
from rest_framework import routers

from .views import HomeView, PersonView, QuestionsView, QuestionsViewSet

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('person/', PersonView.as_view(), name='person'),
    # ApiView
    path('questions/', QuestionsView.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionsView.as_view(), name='questions_pk'),
]

# ViewSet
router = routers.DefaultRouter()
router.register(r'questionsviewset', QuestionsViewSet, basename='questionsviewset')
urlpatterns += router.urls
