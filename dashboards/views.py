from django.shortcuts import render
from django.contrib.messages import get_messages
from answers.models import AnswersModel
from authentication.models import UserData
from authentication.decorators import admin_role_required, user_role_required

from django.views.generic import View


class AdminView(View):

    @admin_role_required
    def get(self, request):
        # Render Admin dashboard with error/success messages
        messages = get_messages(request)
        view_message = None
        for message in messages:
            view_message = message
        return render(request, 'dashboards/admin_dashboard.html', {'message': view_message})


class UserView(View):

    @user_role_required
    def get(self, request):
        # Render User dashboard
        departments = UserData.objects.get(f_auth_id=request.user.id).departmentsmodel_set.all()
        if not departments:
            # Show message if user haven't any test yet
            return render(request, 'dashboards/user_dashboard.html', {'msg': True})
        messages = get_messages(request)
        view_message = None
        for message in messages:
            view_message = message
        passed = AnswersModel.objects.filter(f_user=request.user.id).exists()
        return render(request, 'dashboards/user_dashboard.html', {'departments': departments,
                                                                  'passed': passed})
