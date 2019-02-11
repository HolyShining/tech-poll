from django.views.generic import View
from django.shortcuts import render, redirect
from actions.models import QuestionsModel, DepartmentsModel
from django.contrib import messages

from authentication.decorators import admin_role_required


class CreateDepartmentsView(View):
    @admin_role_required
    def get(self, request):
        # Get all questions and load it into select tag
        questions = QuestionsModel.objects.all()
        return render(request, 'actions/form_departments.html', {'questions': questions})

    @admin_role_required
    def post(self, request):
        # Fetch name and connect selected questions to new department
        department = DepartmentsModel()
        department.name = request.POST['name']
        department.save()
        for question in map(int, request.POST.getlist('questions')):
            department.questions.add(QuestionsModel.objects.get(id=question))
        # Show message if adding successful
        messages.add_message(request,
                             messages.SUCCESS,
                             'Department "{}" created successfully!'.format(department.name))
        department.save()
        return redirect('auth-routing')
