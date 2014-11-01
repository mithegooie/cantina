# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('last_4_digits', models.CharField(max_length=4, null=True, blank=True)),
                ('stripe_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('rank', models.CharField(max_length=50, default='Padwan')),
                ('badges', models.ManyToManyField(to='main.Badge')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),

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
