from rest_framework import serializers
from .models import Task, Userlist
from .models import Quiz
from .models import Report

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'work','isComplete','image')



class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'work','title','image')

class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlist
        fields = ('id', 'nickname','password','location', 'email', 'point')
