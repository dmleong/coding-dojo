from django.db import models

class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')
    class Meta:
        db_table = 'questions'
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.TextField(max_length=200)
    class Meta:
        db_table='choices'
