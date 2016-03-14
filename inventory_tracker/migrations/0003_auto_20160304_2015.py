# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0002_auto_20160304_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'statuses'},
        ),
        migrations.AlterField(
            model_name='claim',
            name='claim_confirmation_number',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='claim_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='claim',
            name='claim_paid_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 14, 35, 83364, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='claim',
            name='submitted_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 14, 42, 507873, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='bid_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 14, 46, 748118, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='contract_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 14, 51, 300247, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='environmental_report_received',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 14, 56, 404274, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='environmental_report_submitted',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 14, 59, 956252, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='landmarks_clearance_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 15, 3, 404631, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='preinspection_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 15, 6, 956754, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='public_notice_data',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 15, 10, 796823, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='quiet_title_attorney',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='quiet_title_ordered_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 15, 14, 628981, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='sold_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 20, 15, 18, 733080, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
