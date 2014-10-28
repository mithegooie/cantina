# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
    ]
