
from django.urls import path,include
from .views import *


urlpatterns = [

    path('questions_list/',QuestionsListAPIView.as_view(),name = 'questions_list'),


    path('answer_create/',AnswerPostAPIView.as_view(),name = 'answer_create'),

    path('answer/<int:pk>/',AnswerPUTAPIView.as_view(),name = 'answer_update'),

    path('person/',PersonPostAPIView.as_view(),name = 'person_create'),

    path('person_list/',PersonListAnswerLIstAPIView.as_view(),name = 'person_list'),

    path('survey_list/',SurveyListAPIView.as_view(),name = 'survey_list'),

    path('doc_create/',DocCreateAPIView.as_view(),name = 'doc_creaet'),

    path('notes/',NotesListAPIView.as_view(),name = 'notes_list'),

    path('notes_create/',NotesCreateAPIVIew.as_view(),name = 'notes_create'),

    path('training_material/',Training_materialsListAPIView.as_view(),name = 'training_list'),

    path('training_material/<int:pk>/', Training_materialsListAPIView.as_view(), name='training_list'),

]


# urlpatterns = [
#     path('questions_create/',QuestionsPostAPIView.as_view(),name = 'question_create'),
#     path('questions_list/',QuestionsListAPIView.as_view(),name = 'questions_list'),
#
#
#     path('answer_create/',AnswerPostAPIView.as_view(),name = 'answer_create'),
#
#     path('answer_list/',AnswerListAPIView.as_view(),name = 'answer_list'),
#
# ]