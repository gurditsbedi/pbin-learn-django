# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_auto_20161023_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastemodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
