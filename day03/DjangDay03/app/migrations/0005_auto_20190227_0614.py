# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-02-27 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190227_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='i_person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Person'),
        ),
    ]
