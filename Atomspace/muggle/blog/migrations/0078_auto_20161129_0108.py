# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0077_auto_20161129_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('like', 'like'), ('normal', 'normal')], max_length=10),
        ),
    ]
