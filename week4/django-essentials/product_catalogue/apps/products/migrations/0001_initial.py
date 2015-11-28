# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.TextField(max_length=100)),
                ('product_name', models.TextField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 27, 22, 35, 34, 185306))),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
