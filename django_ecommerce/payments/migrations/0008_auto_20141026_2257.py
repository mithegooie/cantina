# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_auto_20141025_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.CharField(max_length=50, default='Padwan'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unpaidusers',
            name='last_notification',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 26, 22, 57, 40, 140349)),
        ),
    ]
