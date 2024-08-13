from django.urls import path

from .views import HomeView, PersonView, QuestionsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('person/', PersonView.as_view(), name='person'),
    path('questions/', QuestionsView.as_view(), name='questions'),
]
