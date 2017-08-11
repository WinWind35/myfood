# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Menu
from .models import Afterwork

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'cooker')
    list_filter = ('type', 'cooker')
    search_fields = ('name', 'type', 'cooker')
    fieldsets = (
        (None,{
            'fields':(
                ('name','type'),
                'cooker',
            )
        }),
    )

class AfterworkAdmin(admin.ModelAdmin):
    list_display = ('clean', 'fruit')
    list_filter = ('clean', 'fruit')
    search_fields = ('clean', 'fruit')
    fieldsets = (
        (None,{
            'fields':(
                'clean',
                'fruit',
            )
        }),
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(Afterwork, AfterworkAdmin)