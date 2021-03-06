# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dgcrm', '0007_auto_20170619_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dgcrm.Client'),
        ),
        migrations.AddField(
            model_name='result',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dgcrm.Event'),
        ),
    ]
