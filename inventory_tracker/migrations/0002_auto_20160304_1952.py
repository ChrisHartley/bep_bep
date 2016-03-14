# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'properties'},
        ),
        migrations.AddField(
            model_name='claim',
            name='claim_paid_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 19, 52, 52, 499734, tzinfo=utc)),
            preserve_default=False,
        ),
#        migrations.AlterField(
#            model_name='claim',
#            name='claim_paid',
#            field=models.BooleanField(),
#        ),

	migrations.RemoveField(
		model_name='claim',
		name='claim_paid',
	),
	migrations.AddField(
		model_name='claim',
		name='claim_paid',
		field=models.BooleanField(),
	),

        migrations.AlterField(
            model_name='claim',
            name='submitted_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bid_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='contract_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='environmental_report_received',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='environmental_report_submitted',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='landmarks_clearance_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='preinspection_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='public_notice_data',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='quiet_title_ordered_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='quiet_title_status',
            field=models.IntegerField(default=3, choices=[(1, b'Quiet Title Complete'), (2, b'Quiet Title Action Ordered'), (3, b'No Quiet Title')]),
        ),
        migrations.AlterField(
            model_name='property',
            name='sold_date',
            field=models.DateField(null=True),
        ),
    ]
