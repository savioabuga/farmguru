# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_transaction_transaction_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='group',
            new_name='animalgroup',
        ),
    ]
