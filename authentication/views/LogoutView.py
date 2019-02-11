from django.contrib import auth
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    def post(self, request):
        # Destroy user session
        auth.logout(request)
        return redirect('home-page')

    def get(self, request, *args, **kwargs):
        # If someone tries to GET /login, raise 404 error
        raise Http404
