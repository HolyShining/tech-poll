from django.shortcuts import redirect
from django.urls import NoReverseMatch
from django.views.generic import View
from authentication import models


class Routing(View):
    def get(self, request):
        # Autoredirect user by his role, if system can't recognize role - send user to homepage
        role = models.UserData.objects.get(f_auth_id=request.user.id).f_role.name
        try:
            return redirect('{}-dashboard'.format(role.lower()))
        except NoReverseMatch:
            return redirect('home-page')
