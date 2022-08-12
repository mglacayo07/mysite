import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20,default="superadmin")
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=20, default="superadmin")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def who(self):
        return self.created_by

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, default="superadmin")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20, default="superadmin")

    def __str__(self):
        return self.choice_text

    def who(self):
        return self.created_by