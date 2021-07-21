# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(default=b'income', max_length=20, choices=[(b'income', 'Income'), (b'expense', 'Expense')]),
            preserve_default=True,
        ),
    ]
