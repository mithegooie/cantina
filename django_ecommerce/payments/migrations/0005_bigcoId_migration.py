# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations


def migrate_bigcoid(apps, schema_editor):
    User = apps.get_model('payments', 'User')

    for u in User.objects.all():
        bid = ("{}{}{}{}".format(u.name[:2],
                                 u.rank[:1],
                                 u.created_at.strftime("%m%d%Y"),
                                 u.id))
        u.bigCoID = bid
        u.save()

class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20141101_1034'),
    ]

    operations = [
        migrations.RunPython(migrate_bigcoid)
    ]
