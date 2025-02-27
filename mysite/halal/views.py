from django.shortcuts import render
from rest_framework.viewsets import generics

from .serializer import *

class SurveyListAPIView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class QuestionsListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsListSerializer


class PersonPostAPIView(generics.CreateAPIView):
    serializer_class = PersonSerializer


class PersonListAnswerLIstAPIView(generics.ListAPIView):
    serializer_class = PersonListSerializer
    queryset = PersonResponse.objects.all()


class AnswerPostAPIView(generics.CreateAPIView):
    serializer_class = AnswerPostSerializer

class AnswerPUTAPIView(generics.UpdateAPIView):
    serializer_class = AnswerPUTSerializer
    queryset = Answer.objects.all()


class DocCreateAPIView(generics.CreateAPIView):
    serializer_class = DocumentsCreateSerializer

















# from django.shortcuts import render
# from rest_framework.viewsets import generics
#
# from .serializer import *
#
#
# class QuestionsPostAPIView(generics.CreateAPIView):
#     serializer_class = QuestionCreateSerializer
#
#
# class QuestionsListAPIView(generics.ListAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionsListSerializer
#
# class AnswerPostAPIView(generics.CreateAPIView):
#     serializer_class = AnswerPostSerializer
#
#
# class AnswerListAPIView(generics.ListAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerListSerializer


