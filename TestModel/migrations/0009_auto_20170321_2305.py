# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-21 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0008_user_stu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='stu_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
