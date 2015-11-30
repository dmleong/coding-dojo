# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 21, 4, 26, 271870, tzinfo=utc), verbose_name=datetime.datetime(2015, 11, 30, 21, 4, 3, 359638)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 30, 21, 4, 3, 358264)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 30, 21, 4, 3, 358953)),
        ),
    ]
