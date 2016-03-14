# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_tracker', '0010_claim_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='submitted_date',
            new_name='date',
        ),
    ]
