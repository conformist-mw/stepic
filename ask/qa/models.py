from django.db import models, connection
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new():
        pass

    def popular():
        pass


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    autor = models.CharField(max_length=50)
    likes = models.IntegerField()
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    autor = models.CharField(max_length=50)
