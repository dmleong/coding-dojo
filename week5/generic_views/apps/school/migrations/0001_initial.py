# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 30, 19, 2, 8, 606475))),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=100)),
                ('student', models.ManyToManyField(to='school.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 30, 19, 2, 8, 607156))),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(to='school.Teacher'),
        ),
    ]
