# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0005_auto_20160304_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bid_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='contract_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='environmental_report_received',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='environmental_report_submitted',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='landmarks_clearance_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='preinspection_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='public_notice_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='quiet_title_ordered_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='sold_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
