# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-19 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20161019_0444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='save',
            new_name='save_search',
        ),
        migrations.AlterField(
            model_name='search',
            name='name',
            field=models.CharField(default='Unsaved Search 2016-10-19 11:52:07.230166+00:00', max_length=100),
        ),
    ]
