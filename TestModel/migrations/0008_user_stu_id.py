# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-21 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0007_auto_20170311_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TestModel.Students'),
        ),
    ]
