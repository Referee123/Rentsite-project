# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentsite', '0002_auto_20170324_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartament',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='apartament',
            name='image',
            field=models.TextField(blank=True, max_length=750, null=True),
        ),
    ]
