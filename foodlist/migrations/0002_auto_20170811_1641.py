# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='cooker',
            field=models.IntegerField(choices=[(0, '跟班小王'), (1, '张大厨')], verbose_name='制作人'),
        ),
    ]
