from django.db import models
from user.models import UserProfile

from django.db.models import Count, Case, When, IntegerField


class Survey(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)



class Question(models.Model):
    person = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE,related_name='questions')

    def __str__(self):
        return self.text




class PersonResponse(models.Model):
    person = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return f'{self.person}'

    @property
    def readiness(self):
        answers = self.answer.all()
        total_questions = answers.count()

        if total_questions == 0:
            return {
                "readiness": 0,
                "meets_requirements": 0,
                "in_progress": 0,
                "needs_improvement": 0
            }

        stats = answers.aggregate(
            yes_count=Count(Case(When(response='yes', then=1), output_field=IntegerField())),
            in_progress_count=Count(Case(When(response='in_progress', then=1), output_field=IntegerField())),
            no_count=Count(Case(When(response='no', then=1), output_field=IntegerField())),
        )

        yes_percentage = (stats['yes_count'] / total_questions) * 100
        in_progress_percentage = (stats['in_progress_count'] / total_questions) * 100
        no_percentage = (stats['no_count'] / total_questions) * 100

        return {
            "Готовность": round(yes_percentage),
            "Соответствует требованиям": round(yes_percentage),
            "В процессе улучшений": round(in_progress_percentage),
            "Требует доработки": round(no_percentage)
        }



class Answer(models.Model):
    RESPONSE_CHOICES = [
        ('yes', 'Да'),
        ('in_progress', 'В процессе'),
        ('no', 'Нет')
    ]

    person = models.ForeignKey(PersonResponse, on_delete=models.CASCADE, related_name='answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=20, choices=RESPONSE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.question} - {self.response}"



class Documents(models.Model):
    doc = models.FileField(upload_to='documents',null=True,blank=True)
    author = models.ForeignKey(PersonResponse,on_delete=models.CASCADE,related_name='documents')
    created_date = models.DateTimeField(auto_now_add=True)

from django.db import models
from user.models import UserProfile


class Question(models.Model):
    person = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    RESPONSE_CHOICES = [
        ('yes', 'Да'),
        ('in_progress', 'В процессе'),
        ('no', 'Нет')
    ]


    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=20, choices=RESPONSE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.question} - {self.response}"


class SurveyResult(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    total_questions = models.IntegerField()
    yes_count = models.IntegerField()
    yes_percent = models.DecimalField(max_digits=5, decimal_places=2)
    in_progress_count = models.IntegerField()
    no_count = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.percentage}% готовности"
