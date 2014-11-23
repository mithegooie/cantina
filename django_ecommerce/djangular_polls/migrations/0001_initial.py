# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=300)),
                ('votes', models.IntegerField(default=0)),
                ('percentage', models.DecimalField(default=0.0, decimal_places=2, max_digits=5)),
                ('poll', models.ForeignKey(related_name='items', to='djangular_polls.Poll')),
            ],
            options={
                'ordering': ['-text'],
            },
            bases=(models.Model,),
        ),
    ]
