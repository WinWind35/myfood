# coding:utf-8
from __future__ import unicode_literals

from django import forms

from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = (
            'name', 'type', 'cooker',
        )