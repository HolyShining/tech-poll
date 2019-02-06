from django.contrib import messages
from django.views.generic import View
from django.shortcuts import render, redirect
from authentication.models import UserData
from actions.models import DepartmentsModel


class AddUserToDepartment(View):
    def get(self, request):
        users = UserData.objects.all()
        departments = DepartmentsModel.objects.all()
        return render(request, 'actions/form_departments_attach.html', {'users': users,
                                                                        'departments': departments})

    def post(self, request):
        dep = DepartmentsModel.objects.get(id=request.POST['department'])
        dep.users.add(UserData.objects.get(id=request.POST['selected_user']))
        messages.add_message(request,
                             messages.SUCCESS,
                             '{} and {} connected successfully!'.format(dep.name,
                                                                        UserData.objects.get(id=request.POST['selected_user'])))
        dep.save()
        return redirect('auth-routing')
