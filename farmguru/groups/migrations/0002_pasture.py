# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20150409_0625'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('acreage', models.IntegerField(max_length=10, null=True, blank=True)),
                ('members', models.ManyToManyField(related_name='pastures', null=True, to='animals.Animal', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
