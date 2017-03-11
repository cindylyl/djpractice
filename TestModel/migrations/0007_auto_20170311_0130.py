# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-11 01:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0006_delete_gain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gain_date', models.DateField(default=datetime.date.today)),
                ('rank_id', models.ForeignKey(default=5001, on_delete=django.db.models.deletion.CASCADE, to='TestModel.Rank')),
                ('stu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TestModel.Students')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gain',
            unique_together=set([('stu_id', 'rank_id')]),
        ),
    ]
