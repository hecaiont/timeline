from django.shortcuts import render

from django.views.generic import ListView

from .models import *

class ResumeView(ListView):
    # context_object_name = 'name'
    # template_name = 'page/path.html'
    queryset = Achievement.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['Profile'] = Profile.objects.all()
        context['Achievement'] = self.queryset
        
        return context