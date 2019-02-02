from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import View
from . import models
from .models import SectionsModel, StagesModel, QuestionsModel


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return redirect('home-view')


class SectionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'actions/create_sections.html')

    def post(self, request):
        section = models.SectionsModel(name=request.POST['name'])
        print(section)
        messages.add_message(request,
                             messages.SUCCESS,
                             'Section "{}" created successfully!'.format(section.name))
        section.save()
        return redirect('auth-routing')


class StageView(View):
    def get(self, request):
        sections = SectionsModel.objects.all()
        return render(request, 'actions/create_stages.html', {'sections': sections})

    def post(self, request):
        stage = StagesModel(name=request.POST['name'])
        stage.f_section_id = request.POST['section']
        messages.add_message(request,
                             messages.SUCCESS,
                             'Section "{}" created successfully!'.format(stage.name))
        stage.save()
        return redirect('auth-routing')


class QuestionView(View):
    def get(self, request):
        stages = StagesModel.objects.all()
        return render(request, 'actions/create_questions.html', {'stages': stages})

    def post(self, request):
        question = QuestionsModel(name=request.POST['name'], hint=request.POST['hint'])
        question.f_stage_id = request.POST['stage']
        messages.add_message(request,
                             messages.SUCCESS,
                             'Question "{}" created successfully!'.format(question.name))
        question.save()
        return redirect('auth-routing')
