from django.db import models
from datetime import datetime


class Student(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    created_at = models.DateTimeField(datetime.now())


class Teacher(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    created_at = models.DateTimeField(datetime.now())


class Subject(models.Model):
    title = models.TextField(max_length=100)
    teacher = models.ForeignKey(Teacher)
    student = models.ManyToManyField(Student)
    created_at = models.DateTimeField(datetime.now())
