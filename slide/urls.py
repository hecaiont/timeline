from django.urls import path

from slide.views import ResumeView

urlpatterns = [
    path('', ResumeView.as_view(), name='ResumeView'),
]