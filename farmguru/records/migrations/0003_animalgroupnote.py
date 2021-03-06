# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_pasture'),
        ('records', '0002_animaldocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalGroupNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('date', models.DateField(null=True, blank=True)),
                ('file', models.FileField(null=True, upload_to=b'notes', blank=True)),
                ('details', models.TextField(blank=True)),
                ('animalgroup', models.ForeignKey(to='groups.AnimalGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
