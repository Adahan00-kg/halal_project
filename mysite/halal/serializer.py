from rest_framework import serializers
from .models import *
from user.serializers import UserProfileSerializer


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['title']


class QuestionsListSerializer(serializers.ModelSerializer):
    person = UserProfileSerializer()
    class Meta:
        model = Question
        fields = ['id','person','text']


class QuestionsSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonResponse
        fields = ['person']


class AnswerPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['person','question','response']


class AnswerPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['response']

class DocListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ['doc']

class AnswerListSerializer(serializers.ModelSerializer):
    question = QuestionsSimpleSerializer()
    class Meta:
        model = Answer
        fields = ['id','question','response']


class PersonListSerializer(serializers.ModelSerializer):
    answer = AnswerListSerializer(many=True)
    person = UserProfileSerializer()
    readiness = serializers.ReadOnlyField()
    documents = DocListSerializer(many=True)
    class Meta:
        model = PersonResponse
        fields = ['person','answer','readiness','documents']

class DocumentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ['doc','author']


class NotesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields= ['author','notes_title','status','date']


class NotesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['notes_title','status','date']


class Training_materialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training_materials
        fields = ['materials_title','content']


# from rest_framework import serializers
# from .models import *
# from user.serializers import UserProfileSerializer
#
# class QuestionCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ['person','text']
#
# class QuestionsListSerializer(serializers.ModelSerializer):
#     person = UserProfileSerializer()
#     class Meta:
#         model = Question
#         fields = ['id','person','text']
#
# class QuestionsSimpleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ['text']
#
# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonResponse
#         fields = ['']
# class AnswerPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ['user','question','response']
#
#
# class AnswerListSerializer(serializers.ModelSerializer):
#     user = UserProfileSerializer()
#     question = QuestionsSimpleSerializer()
#     class Meta:
#         model = Answer
#         fields = ['user','question','response']

