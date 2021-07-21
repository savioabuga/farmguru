# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_pasture'),
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalGroupTreatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('type', models.CharField(max_length=20, choices=[(b'vaccination', 'Vaccination')])),
                ('date', models.DateField(null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('animal', models.ForeignKey(to='groups.AnimalGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='grouptreatment',
            name='animal',
        ),
        migrations.DeleteModel(
            name='GroupTreatment',
        ),
    ]
