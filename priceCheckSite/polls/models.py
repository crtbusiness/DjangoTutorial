import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text #Database returns human-readable info with this function
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now #This should check if the time is in the future
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #lets us know if an entry was entered within a day as of current
#Field classes (e.g. Charfield or DateTimeField) tell Django what type of data each field holds
#Database will use the variable name as a column name in the DB
#We can also use an optional first-position argument to name our fields such as with pub_date

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
#ForeignKey defines a database relationship
#In this case, a Choice object is linked to a Question object