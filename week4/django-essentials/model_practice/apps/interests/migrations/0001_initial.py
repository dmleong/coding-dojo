# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 24, 1, 45, 32, 929562))),
            ],
            options={
                'db_table': 'interests',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=200)),
                ('last_name', models.TextField(max_length=200)),
                ('age', models.IntegerField()),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 24, 1, 45, 32, 930283))),
                ('occupation', models.TextField(max_length=200)),
                ('interest', models.ForeignKey(to='interests.Interest')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
