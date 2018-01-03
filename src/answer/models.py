from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer_text = models.TextField()
    questions = models.ForeignKey(Question)
    pub_date = models.DateTimeField(auto_now_add=True)
    # upvote = models.IntegerField(null=True, blank=True)

    user = models.ForeignKey(User)

    def __str__(self):
        return self.answer_text

    def get_absolute_url(self):
        return reverse('answer:answer_by_me', kwargs={'pk': self.questions})


class Upvote(models.Model):
    questions = models.ForeignKey(Question)
    answers = models.ForeignKey(Answer)