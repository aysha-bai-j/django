# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 10:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 2, 10, 51, 25, 683282, tzinfo=utc)),
        ),
    ]
