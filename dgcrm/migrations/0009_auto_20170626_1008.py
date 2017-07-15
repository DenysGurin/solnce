# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgcrm', '0008_auto_20170624_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='canceledevent',
            name='brutto_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='total_paid',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
