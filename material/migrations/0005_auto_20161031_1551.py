# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_auto_20161031_1547'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='material',
            unique_together=set([('name', 'type_no')]),
        ),
    ]
