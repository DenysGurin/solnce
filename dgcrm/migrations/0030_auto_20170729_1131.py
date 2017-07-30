# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-29 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgcrm', '0029_auto_20170715_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='detailed_services',
        ),
        migrations.AddField(
            model_name='client',
            name='total_paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
