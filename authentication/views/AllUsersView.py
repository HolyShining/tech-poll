from django.views.generic import View
from django.shortcuts import render
from authentication import models


class AllUsersView(View):
    def get(self, request):
        role = models.UserData.objects.get(f_auth_id=request.user.id).f_role.name
        if role == 'Admin':
            users = models.UserData.objects.all()
        else:
            users = models.UserData.objects.exclude(f_role__name='Admin')
        return render(request, 'authentication/all_users.html', {'users': users})
