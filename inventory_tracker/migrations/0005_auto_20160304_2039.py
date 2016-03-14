# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0004_auto_20160304_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='public_notice_data',
            new_name='public_notice_date',
        ),
    ]
