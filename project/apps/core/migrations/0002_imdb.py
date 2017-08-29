# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-29 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_used', models.BooleanField(default=0)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('imdb_id', 'created_at'),
                'verbose_name': 'IMDB',
                'verbose_name_plural': 'IMDB',
            },
        ),
    ]
