# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='claim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted_date', models.DateField()),
                ('claim_paid', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('claim_confirmation_number', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parcel', models.CharField(max_length=7)),
                ('street_address', models.CharField(max_length=255)),
                ('public_notice_complete', models.BooleanField(default=False)),
                ('public_notice_data', models.DateField()),
                ('landmarks_clearance_date', models.DateField()),
                ('preinspection_complete', models.BooleanField(default=False)),
                ('preinspection_date', models.DateField()),
                ('environmental_report_complete', models.BooleanField(default=False)),
                ('environmental_report_submitted', models.DateField()),
                ('environmental_report_received', models.DateField()),
                ('bid_date', models.DateField()),
                ('bid_group', models.CharField(max_length=25)),
                ('contract_date', models.DateField()),
                ('sold_date', models.DateField()),
                ('quiet_title_status', models.IntegerField(choices=[(1, b'Quiet Title Complete'), (2, b'Quiet Title Action Ordered'), (3, b'No Quiet Title')])),
                ('quiet_title_attorney', models.CharField(max_length=255)),
                ('quiet_title_ordered_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(choices=[(1, b'Some party has requested that the property be added to BEP'), (2, b'Renew Indianapolis rejected the request to add the property to BEP'), (3, b'Add request submitted to IHCDA'), (4, b'IHCDA added the property to BEP'), (5, b'IHCDA rejected the BEP add request'), (6, b'Some party has requested that the property be removed from BEP'), (7, b'Renew Indianapolis rejected the rqeuest to remove the property from BEP'), (8, b'Remove request submitted to IHCDA')])),
                ('note', models.CharField(max_length=255, blank=True)),
                ('prop', models.ForeignKey(to='inventory_tracker.Property')),
            ],
        ),
        migrations.AddField(
            model_name='claim',
            name='prop',
            field=models.ForeignKey(to='inventory_tracker.Property'),
        ),
    ]
