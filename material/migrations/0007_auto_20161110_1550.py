# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0006_auto_20161110_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmaterial',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='\u5165\u5e93\u6570\u91cf'),
        ),
    ]
