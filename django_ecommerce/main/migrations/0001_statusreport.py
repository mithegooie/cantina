# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_auto_20141027_0722'),
        ('main', 'data_load_marketing_items_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusReport',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to='payments.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
