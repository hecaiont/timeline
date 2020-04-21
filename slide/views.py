from django.shortcuts import render

from .models import Achievement

def AchievementList(request):
    Achievements = Achievement.objects.filter(visible=True)
    return render(request, 'slide/AchievementList.html', {'Achievements' : Achievements})

    