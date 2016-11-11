# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pasteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=8)),
                ('name', models.CharField(default='Unnamed', max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='paste',
        ),
    ]
