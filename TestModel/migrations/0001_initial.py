# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-18 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=100)),
                ('t_method', models.CharField(max_length=100)),
            ],
        ),
    ]
