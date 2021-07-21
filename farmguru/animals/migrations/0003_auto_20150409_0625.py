# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20150329_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasture',
            name='members',
        ),
        migrations.DeleteModel(
            name='Pasture',
        ),
        migrations.AlterField(
            model_name='animal',
            name='ear_tag',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
