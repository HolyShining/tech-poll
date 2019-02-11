from django.contrib import auth, messages
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View


class LoginView(View):
    def post(self, request):
        # If user exists - login, otherwise send 'incorrect password' message
        # And redirect to homepage
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('auth-routing')
        else:
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Password is incorrect')
            return redirect('home-page')

    def get(self, request, *args, **kwargs):
        # If someone tries to GET /login, raise 404 error
        raise Http404
