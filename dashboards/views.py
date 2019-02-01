from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import TemplateView


class AdminView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboards/admin_dashboard.html')


class UserView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboards/user_dashboard.html')
