# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnpaidUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('last_notification', models.DateTimeField(default=datetime.datetime(2014, 10, 21, 23, 29, 28, 775530))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
