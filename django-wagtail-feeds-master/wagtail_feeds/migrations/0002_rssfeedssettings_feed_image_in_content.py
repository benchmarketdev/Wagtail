# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-29 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssfeedssettings',
            name='feed_image_in_content',
            field=models.BooleanField(default=True, help_text=b'Add feed image to content encoded field'),
        ),
    ]
