# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0006_auto_20160304_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='contract_winner',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='property',
            name='demolished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='demolished_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='property',
            name='notes',
            field=models.CharField(max_length=512, blank=True),
        ),
        migrations.AddField(
            model_name='status',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 15, 46, 38, 360767, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='prop',
            field=models.ForeignKey(related_name='status', to='inventory_tracker.Property'),
        ),
    ]
