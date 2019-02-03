from django.views.generic import View
from django.shortcuts import render, redirect
from actions.models import QuestionsModel
from django.contrib import messages


class CreateDepartmentsView(View):
    def get(self, request):
        questions = QuestionsModel.objects.all()
        return render(request, 'actions/form_departments.html', {'questions': questions})

    def post(self, request):
        department = None
        print()
        print(request.POST.getlist('questions'))
        messages.add_message(request,
                             messages.SUCCESS,
                             'Department "{}" created successfully!'.format(request.POST['name']))
        return redirect('auth-routing')
