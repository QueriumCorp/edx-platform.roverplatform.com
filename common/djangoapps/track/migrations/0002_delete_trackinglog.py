# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-04 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrackingLog',
        ),
    ]
