from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import get_messages
from actions.models import DepartmentsModel

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
        departments = DepartmentsModel.objects.all()
        return render(request, 'dashboards/user_dashboard.html', {'departments': departments})
