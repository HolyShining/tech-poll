from django.shortcuts import render, redirect, get_object_or_404
from actions.models import StagesModel, QuestionsModel
from django.contrib import messages
from actions.views import DetailView


class QuestionDetailView(DetailView):
    model = QuestionsModel
    template = 'actions/form_questions.html'
    add_models = StagesModel

    def get(self, request, object_id):
        # Load linked stage for question
        stages = self.add_models.objects.all()
        obj = get_object_or_404(self.model, pk=object_id)
        return render(request, self.template, {'obj': obj,
                                               'stages': stages})

    def post(self, request, object_id):
        # Update question and save changes
        question = get_object_or_404(self.model, pk=object_id)
        question.name = request.POST['name']
        question.hint = request.POST['hint']
        question.f_stage_id = request.POST['stage']
        question.save()
        messages.add_message(request, messages.SUCCESS, 'Question updated successfully')
        return redirect('auth-routing')
