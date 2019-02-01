from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from . import models


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect('home-view')


class SectionView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'actions/create_sections.html')

    def post(self, request):
        section = models.SectionsModel
