from django.db import models
from datetime import datetime

class Interest(models.Model):
    name = models.TextField(max_length=200)
    created_at = models.DateTimeField(datetime.now())
    class Meta:
        db_table = 'interests'

class User(models.Model):
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    age = models.IntegerField()
    created_at = models.DateTimeField(datetime.now())
    occupation = models.TextField(max_length=200)
    interest = models.ForeignKey(Interest)
    class Meta:
        db_table = 'users'
