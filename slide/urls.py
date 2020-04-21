from django.urls import path

from . import views

urlpatterns = [
    path('', views.AchievementList, name='AchievementList'),
]