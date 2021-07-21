# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20150409_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalgrouptreatment',
            old_name='animal',
            new_name='animalgroup',
        ),
    ]
