from __future__ import unicode_literals
from django.db import models
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
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User, through='Likes')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)


class Likes(models.Model):
    question = models.ForeignKey(Question, related_name='like_question')
    user = models.ForeignKey(User, related_name='like_user')
