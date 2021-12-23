from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, TextField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)