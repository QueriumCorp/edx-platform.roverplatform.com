# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-16 14:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0017_remove_start_from_historicalschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalschedule',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historicalschedule',
            name='start_date',
            field=models.DateTimeField(db_index=True, default=None, help_text='Date this schedule went into effect', null=True),
        ),
    ]
