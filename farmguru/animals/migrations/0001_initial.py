# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('animal_id', models.CharField(max_length=30, blank=True)),
                ('alt_id', models.CharField(max_length=30, blank=True)),
                ('electronic_id', models.CharField(max_length=30, blank=True)),
                ('ear_tag', models.CharField(max_length=30, blank=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('color', models.CharField(max_length=20, choices=[(b'yellow', 'Yellow')])),
                ('gender', models.CharField(max_length=20, choices=[(b'male', 'Male'), (b'female', 'Female')])),
                ('status', models.CharField(default=b'active', max_length=20, choices=[(b'active', 'Active')])),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('birth_weight', models.IntegerField(max_length=4, null=True, blank=True)),
                ('weaning_date', models.DateField(null=True, blank=True)),
                ('weaning_weight', models.IntegerField(max_length=4, null=True, blank=True)),
                ('yearling_date', models.DateField(null=True, blank=True)),
                ('yearling_weight', models.IntegerField(max_length=4, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=30)),
                ('gestation_period', models.IntegerField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(blank=True, to='animals.Breed', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='dam',
            field=models.ForeignKey(related_name='animal_dam', blank=True, to='animals.Animal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animal',
            name='sire',
            field=models.ForeignKey(related_name='animal_sire', blank=True, to='animals.Animal', null=True),
            preserve_default=True,
        ),
    ]
