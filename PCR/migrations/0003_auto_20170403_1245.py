# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCR', '0002_patientrecord_alertupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='alertupdate',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]