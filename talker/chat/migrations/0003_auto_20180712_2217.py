# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-12 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_chat_data_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_data',
            name='image',
            field=models.ImageField(default=None, upload_to='pictures'),
        ),
        migrations.AddField(
            model_name='chat_data',
            name='msg',
            field=models.CharField(default=None, max_length=254),
        ),
    ]