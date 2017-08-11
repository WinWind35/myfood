# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):
    COOKER_ITEMS = [
        (0, '跟班小王'),
        (1, '张大厨'),
    ]
    COOKTYPE_ITEMS = [
        (0, '荤'),
        (1, '素'),
    ]
    name = models.CharField(max_length=128, verbose_name="菜名")
    type = models.IntegerField(choices=COOKTYPE_ITEMS, verbose_name="类型")
    cooker = models.IntegerField(choices=COOKER_ITEMS, verbose_name="制作人")

    def __unicode__(self):
        return '<Menu: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "菜单"


class Afterwork(models.Model):
    CLEAN_ITEMS = [
        (0, '小王'),
        (1, '小张'),
    ]
    FRUIT_ITEMS = [
        (0, '没有水果吃'),
        (1, '买水果吃'),
    ]
    clean = models.IntegerField(choices=CLEAN_ITEMS, verbose_name="收拾")
    fruit = models.IntegerField(choices=FRUIT_ITEMS, verbose_name="餐后水果")

    #def __unicode__(self):
        #return '<Afterwork: {}>'.format(self.clean)

    class Meta:
        verbose_name = verbose_name_plural = "餐后工作"