# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View
import random

from .models import Menu, Afterwork
from .forms import MenuForm

# Create your views here.
class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        menu = Menu.objects.all()
        context = {
            'menu': menu,
        }
        return context

    def get(self,request):
        context = self.get_context()
        form = MenuForm()
        context.update({
            'form':form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = MenuForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            menu = Menu()
            menu.name = cleaned_data['name']
            menu.type = cleaned_data['type']
            menu.cooker = cleaned_data['cooker']
            menu.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form,
        })
        return render(request, self.template_name, context=context)


def foodlist(request):
    list_hun = Menu.objects.filter(type=0)
    last_hun = Menu.objects.filter(type=0).count() - 1
    list_su = Menu.objects.filter(type=1)
    last_su = Menu.objects.filter(type=1).count() - 1
    clean = ['小张', '小王']

    food_list = []
    food_dic = {}
    i = 1
    while i < 8:
        index = random.randint(0, last_hun)
        food_hun = list_hun[index]

        index = random.randint(0, last_su)
        food_su = list_su[index]
        food_dic = {
            'week': i,
            'su': food_su.name,
            'cooksu':food_su.get_cooker_display(),
            'hun': food_hun.name,
            'cookhun': food_hun.get_cooker_display(),
            'clean': clean[random.randint(0,1)]
        }
        food_list.append(food_dic)
        i = i + 1

    context = IndexView.get_context(IndexView)
    form = MenuForm()
    context.update({
        'form': form,
        'food_list': food_list,
    })
    return render(request, 'index.html', context=context)
