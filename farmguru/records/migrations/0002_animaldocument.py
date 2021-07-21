# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20150329_1257'),
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('file', models.FileField(max_length=255, upload_to=b'documents')),
                ('deleted', models.BooleanField(default=False)),
                ('animal', models.ForeignKey(related_name='documents', to='animals.Animal')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
