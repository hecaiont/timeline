from django.urls import path

from slide.views import AchievementList

urlpatterns = [
    path('', AchievementList.as_view(), name='AchievementList'),
]