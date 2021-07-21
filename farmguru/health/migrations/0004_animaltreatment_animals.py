# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20150409_0625'),
        ('health', '0003_auto_20150409_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaltreatment',
            name='animals',
            field=models.ManyToManyField(related_name='treatment', to='animals.Animal'),
            preserve_default=True,
        ),
    ]
