# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 23:32
from __future__ import unicode_literals

from django.db import migrations
from temba.sql import InstallSQL


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0052_reset_4'),
    ]

    operations = [
        InstallSQL('0053_channels')
    ]