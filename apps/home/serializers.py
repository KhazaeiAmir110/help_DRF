from rest_framework import serializers

from apps.home.models import Person, Questions, Answer


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
