from django.shortcuts import render, redirect, get_object_or_404
from actions.models import QuestionsModel, DepartmentsModel
from django.contrib import messages
from actions.views import DetailView


class DepartmentsDetailView(DetailView):
    model = DepartmentsModel
    template = 'actions/form_departments.html'
    add_models = QuestionsModel

    def get(self, request, object_id):
        # Load questions for selected departments and render it
        questions = self.add_models.objects.all()
        obj = get_object_or_404(self.model, pk=object_id)
        selected = [q.id for q in DepartmentsModel.objects.get(id=1).questions.all()]
        return render(request, self.template, {'obj': obj,
                                               'questions': questions,
                                               'selected': selected})

    def post(self, request, object_id):
        # Update connected questions
        department = get_object_or_404(self.model, pk=object_id)
        department.name = request.POST['name']
        department.save()
        for question in map(int, request.POST.getlist('questions')):
            department.questions.add(QuestionsModel.objects.get(id=question))
        messages.add_message(request,
                             messages.SUCCESS,
                             'Department "{}" updated successfully!'.format(department.name))
        department.save()
        return redirect('auth-routing')