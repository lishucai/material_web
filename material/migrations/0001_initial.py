# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 00:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'db_table': 'in_material',
                'default_related_name': 'ins',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('type_no', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('count', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='OutMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outs', to='material.Material')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='outs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
                'db_table': 'out_material',
                'default_related_name': 'outs',
            },
        ),
        migrations.AddField(
            model_name='inmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ins', to='material.Material'),
        ),
        migrations.AddField(
            model_name='inmaterial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ins', to=settings.AUTH_USER_MODEL),
        ),
    ]
