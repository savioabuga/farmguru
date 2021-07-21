# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20150409_0625'),
        ('health', '0004_animaltreatment_animals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('date', models.DateField(null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('animals', models.ManyToManyField(related_name='treatment', to='animals.Animal')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TreatmentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='animalgrouptreatment',
            name='animalgroup',
        ),
        migrations.DeleteModel(
            name='AnimalGroupTreatment',
        ),
        migrations.RemoveField(
            model_name='animaltreatment',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='animaltreatment',
            name='animals',
        ),
        migrations.DeleteModel(
            name='AnimalTreatment',
        ),
        migrations.AddField(
            model_name='treatment',
            name='type',
            field=models.ForeignKey(to='health.TreatmentType'),
            preserve_default=True,
        ),
    ]
