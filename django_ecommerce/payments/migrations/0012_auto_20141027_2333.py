# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_badge'),
        ('payments', '0011_auto_20141027_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='badges',
            field=models.ManyToManyField(to='main.Badge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unpaidusers',
            name='last_notification',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 27, 23, 33, 57, 646693)),
        ),
    ]
