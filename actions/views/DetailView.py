from django.shortcuts import render, redirect, get_object_or_404
from actions.models import SectionsModel, StagesModel, QuestionsModel
from django.views.generic import View
from django.contrib import messages


class DetailView(View):
    model = None
    template = None
    add_models = None

    def get(self, request, object_id):
        obj = get_object_or_404(self.model, pk=object_id)
        return render(request, self.template, {'obj': obj})


class SectionDetailView(DetailView):
    model = SectionsModel
    template = 'actions/create_sections.html'

    def post(self, request, section_id):
        section = get_object_or_404(SectionsModel, pk=section_id)
        section.name = request.POST['name']
        section.save()
        messages.add_message(request, messages.SUCCESS, 'Section updated successfully')
        return redirect('auth-routing')


class StageDetailView(DetailView):
    model = StagesModel
    template = 'actions/create_stages.html'
    add_models = SectionsModel

    def get(self, request, object_id):
        obj = get_object_or_404(self.model, pk=object_id)
        sections = self.add_models.objects.all()
        return render(request, self.template, {'obj': obj,
                                               'sections': sections})

    def post(self, request, section_id):
        stage = get_object_or_404(self.model, pk=section_id)
        stage.name = request.POST['name']
        stage.f_section_id = request.POST['section']
        stage.save()
        messages.add_message(request, messages.SUCCESS, 'Stage updated successfully')
        return redirect('auth-routing')


class QuestionDetailView(DetailView):
    model = QuestionsModel
    template = 'actions/create_questions.html'
    add_models = StagesModel

    def get(self, request, object_id):
        stages = self.add_models.objects.all()
        obj = get_object_or_404(self.model, pk=object_id)
        return render(request, self.template, {'obj': obj,
                                               'stages': stages})

    def post(self, request, section_id):
        question = get_object_or_404(self.model, pk=section_id)
        question.name = request.POST['name']
        question.hint = request.POST['hint']
        question.f_stage_id = request.POST['stage']
        question.save()
        messages.add_message(request, messages.SUCCESS, 'Question updated successfully')
        return redirect('auth-routing')
