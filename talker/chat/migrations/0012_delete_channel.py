# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-14 21:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_channel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='channel',
        ),
    ]
