# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-24 15:03
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170124_0351'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='course',
            managers=[
                ('courseMgr', django.db.models.manager.Manager()),
            ],
        ),
    ]