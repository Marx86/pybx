# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('peer.peer',),
        ),
        migrations.AddField(
            model_name='peer',
            name='is_peer',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
