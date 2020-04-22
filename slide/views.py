from django.shortcuts import render

from django.views.generic import ListView

from .models import Achievement

class AchievementList(ListView):
    model = Achievement

    