from django.shortcuts import render
from django.contrib.messages import get_messages
from actions.models import DepartmentsModel
from authentication.models import UserData

# Create your views here.
from django.views.generic import TemplateView


class AdminView(TemplateView):
    def get(self, request, *args, **kwargs):
        messages = get_messages(request)
        view_message = None
        for message in messages:
            view_message = message
        return render(request, 'dashboards/admin_dashboard.html', {'message': view_message})


class UserView(TemplateView):
    def get(self, request, *args, **kwargs):
        departments = UserData.objects.get(f_auth_id=request.user.id).departmentsmodel_set.all()
        print(departments)
        messages = get_messages(request)
        view_message = None
        for message in messages:
            view_message = message
        print(view_message)
        return render(request, 'dashboards/user_dashboard.html', {'departments': departments})
