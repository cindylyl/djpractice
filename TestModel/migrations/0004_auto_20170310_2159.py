# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-10 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0003_auto_20170310_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='stu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestModel.Students'),
        ),
    ]