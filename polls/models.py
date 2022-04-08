import datetime
from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib import admin
from autoslug import AutoSlugField


class Question(models.Model):
    #............WE CAN ASSIGN USER DEFIND VARIABLES NAME TO ADMIN..............
    question_text = models.CharField('Questions HERE',max_length=255)
    pub_date = models.DateTimeField('date published')
    slug = AutoSlugField(populate_from='question_text',unique=True , null=True)



    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):   
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=210)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text


