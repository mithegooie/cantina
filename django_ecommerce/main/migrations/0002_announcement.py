# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_statusreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('when', models.DateTimeField(auto_now=True)),
                ('img', models.CharField(max_length=255, null=True)),
                ('vid', models.URLField(null=True)),
                ('info', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
