# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0007_auto_20160307_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim_paid_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
