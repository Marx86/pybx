# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer', '0002_auto_20160624_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer',
            name='busylevel',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='call_limit',
            field=models.PositiveIntegerField(blank=True, db_column='call-limit', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'Russian'), ('ru', 'English')], default='en', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='lastms',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='maxcallbitrate',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='qualifyfreq',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='regseconds',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='peer',
            name='rtpholdtimeout',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='rtpkeepalive',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='rtptimeout',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='session_expires',
            field=models.IntegerField(blank=True, db_column='session-expires', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='session_minse',
            field=models.IntegerField(blank=True, db_column='session-minse', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='timerb',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='peer',
            name='timert1',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
