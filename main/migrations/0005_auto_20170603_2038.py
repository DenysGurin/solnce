# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='service_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ServiceCategory'),
        ),
    ]
