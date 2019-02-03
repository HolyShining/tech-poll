from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.views.generic import View
from . import models
from .models import SectionsModel, StagesModel, QuestionsModel
from .file import file_worker


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


class DepartmentsView(View):
    def get(self, request):
        questions = QuestionsModel.objects.all()
        return render(request, 'actions/create_departments.html', {'questions': questions})

    def post(self, request):
        department = None
        print(QuestionsModel.objects.filter(id__in=[1,2]))
        print(request.POST.getlist('questions'))
        messages.add_message(request,
                             messages.SUCCESS,
                             'Department "{}" created successfully!'.format(request.POST['name']))
        return redirect('auth-routing')


class LoadFileView(View):
    def get(self, request, mode):
        return render(request, 'actions/load_from_file.html', {'mode': mode})

    def post(self, request, mode):
        file = request.FILES['loaded_file']
        file_context = file_worker(file)
        query_list = []

        if mode == 'section':
            for line in file_context:
                if not SectionsModel.objects.filter(name=line[0]).exists():
                    query_list.append(SectionsModel(name=line[0]))
                return redirect('load-file')
            if query_list:
                StagesModel.objects.bulk_create(query_list)

        if mode == 'stage':
            for line in file_context:
                try:
                    section_id = SectionsModel.objects.get(name=line[1]).pk
                    print(line[0], section_id)
                    if not StagesModel.objects.filter(name=line[0]).exists():
                        query_list.append(StagesModel(name=line[0], f_section_id=section_id))
                except SectionsModel.DoesNotExist:
                    messages.add_message(request,
                                         messages.ERROR,
                                         '{} does not exist'.format(line[1]))
                    return redirect('load-file')
            if query_list:
                StagesModel.objects.bulk_create(query_list)

        if mode == 'question':
            for line in file_context:
                if len(line) == 3:
                    name = line[0]
                    hint = line[1]
                    stage_id = StagesModel.objects.get(name=line[2]).pk
                else:
                    name = line[0]
                    hint = ""
                    stage_id = StagesModel.objects.get(name=line[1]).pk

                try:
                    if not StagesModel.objects.filter(name=name).exists():
                        query_list.append(QuestionsModel(name=name, hint=hint, f_stage_id=stage_id))
                except SectionsModel.DoesNotExist:
                    messages.add_message(request,
                                         messages.ERROR,
                                         '{} does not exist'.format(line[1]))
                    return redirect('load-file')
            if query_list:
                QuestionsModel.objects.bulk_create(query_list)

        messages.add_message(request,
                             messages.SUCCESS,
                             'File successfully loaded!')
        return redirect('auth-routing')
