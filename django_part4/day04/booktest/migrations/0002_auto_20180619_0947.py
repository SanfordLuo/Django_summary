# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='heroinfo',
            options={'verbose_name': '英雄', 'verbose_name_plural': '英雄'},
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='face',
            field=models.ImageField(blank=True, null=True, upload_to='booktest'),
        ),
    ]
