from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import View
from actions.models import GradesModel
from authentication.decorators import admin_role_required


class CreateGradeView(View):

    def get(self, request):
        return render(request, 'actions/form_grade.html')

    def post(self, request):
        grade = GradesModel(name=request.POST['name'])
        print(grade)
        messages.add_message(request,
                             messages.SUCCESS,
                             'Section "{}" created successfully!'.format(grade.name))
        grade.save()
        return redirect('auth-routing')
