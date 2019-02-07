from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import View
from actions.models import StagesModel, QuestionsModel
from authentication.decorators import admin_role_required


class CreateQuestionView(View):
    @admin_role_required
    def get(self, request):
        stages = StagesModel.objects.all()
        return render(request, 'actions/form_questions.html', {'stages': stages})

    @admin_role_required
    def post(self, request):
        question = QuestionsModel(name=request.POST['name'], hint=request.POST['hint'])
        question.f_stage_id = request.POST['stage']
        messages.add_message(request,
                             messages.SUCCESS,
                             'Question "{}" created successfully!'.format(question.name))
        question.save()
        return redirect('auth-routing')
