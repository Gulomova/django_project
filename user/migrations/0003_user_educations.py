# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-18 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200218_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='educations',
            field=models.TextField(blank=True, null=True),
        ),
    ]