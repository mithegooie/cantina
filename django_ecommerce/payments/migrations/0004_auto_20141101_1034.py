# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bigCoID',
            field=models.CharField(default='foo', max_length=50),
            preserve_default=False,
        ),
    ]
