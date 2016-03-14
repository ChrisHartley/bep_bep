# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0008_auto_20160307_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='originally_county_surplus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='originally_privately_owned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='originally_renew_owned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='site_control',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='claim',
            name='submitted_date',
            field=models.DateField(),
        ),
    ]
