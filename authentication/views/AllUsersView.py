from django.views.generic import View
from django.shortcuts import render
from authentication import models
from authentication.decorators import admin_role_required


class AllUsersView(View):

    @admin_role_required
    def get(self, request):
        # Load all users and show up
        users = models.UserData.objects.all()
        return render(request, 'authentication/all_users.html', {'users': users})
