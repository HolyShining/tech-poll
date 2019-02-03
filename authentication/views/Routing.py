from django.shortcuts import redirect
from django.views.generic import View
from authentication import models


class Routing(View):
    def get(self, request):
        role = models.UserData.objects.get(f_auth_id=request.user.id).f_role.name
        if role == 'User':
            return redirect('user-dashboard')
        if role == 'Admin':
            return redirect('admin-dashboard')
        return redirect('home-page')
