from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.conf import settings
from home.models import PortfolioItem, Technology
from django.shortcuts import render
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/main.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['project_list'] = PortfolioItem.objects.all()

        return context
