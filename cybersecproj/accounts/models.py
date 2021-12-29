from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)

class UserSecurityQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
