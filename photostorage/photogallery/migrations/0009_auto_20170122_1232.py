# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0008_auto_20170122_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]