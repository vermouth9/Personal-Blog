# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 18:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 29, 18, 18, 54, 19007, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 29, 18, 18, 54, 19007, tzinfo=utc)),
        ),
    ]
