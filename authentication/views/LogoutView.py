from django.contrib import auth
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect('home-page')

    def get(self, request, *args, **kwargs):
        raise Http404
