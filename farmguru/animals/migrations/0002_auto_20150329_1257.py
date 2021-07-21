# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='color',
            field=models.CharField(blank=True, max_length=20, choices=[(b'yellow', 'Yellow')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(max_length=20, choices=[(b'bull', 'Bull'), (b'cow', 'Cow')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='animal',
            name='status',
            field=models.CharField(default=b'active', max_length=20, blank=True, choices=[(b'active', 'Active')]),
            preserve_default=True,
        ),
    ]
