# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0003_auto_20160304_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bid_group',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]
