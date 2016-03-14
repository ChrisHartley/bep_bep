# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0011_auto_20160310_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='original_private_owner_name',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
