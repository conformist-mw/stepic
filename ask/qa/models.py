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
    author = models.ForeignKey(User, related_name='question_autor')
    likes = models.ManyToManyField(User, through='Likes',
                                   related_name='question_likes')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, related_name='question_answer')
    author = models.ForeignKey(User, related_name='answer_autor')


class Likes(models.Model):
    question = models.ForeignKey(Question, related_name='like_question')
    user = models.ForeignKey(User, related_name='like_user')
