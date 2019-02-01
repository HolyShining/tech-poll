from django.contrib.auth.models import User
from django.contrib import auth
from django.http import Http404
from django.shortcuts import render, redirect
from . import models
from .PasswordGenerator import get_password, randint

# Create your views here.
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentication/createuser.html', {})

    def post(self, request):
        usrname = request.POST['name'][:1] + request.POST['surname'][:4]
        pswrd = get_password(8)
        print("User:{} Password:{}".format(usrname, pswrd))
        try:
            User.objects.get(username=usrname)
            print("*** {} NOT EXIST ***".format(usrname.upper()))
        except User.DoesNotExist:
            pass
        else:
            usrname += str(randint(0, 9))
            print("*** {} EXIST ***".format(usrname.upper()))
        new_user = User.objects.create_user(username=usrname,
                                            password=pswrd)
        new_user.save()
        data = models.UserData(name=request.POST['name'],
                               surname=request.POST['surname'],
                               encrypted_pass=pswrd,
                               fAuth=new_user)
        data.save()
        return render(request, 'authentication/user_created.html', {
            'username': usrname,
            'password': pswrd
        })


class LoginView(TemplateView):
    def post(self, request):
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('auth-routing')
        else:
            return redirect('home-page')

    def get(self, request, *args, **kwargs):
        raise Http404


class LogoutView(TemplateView):
    def post(self, request):
        auth.logout(request)
        return redirect('home-page')

    def get(self, request, *args, **kwargs):
        raise Http404


class Routing(TemplateView):
    def get(self, request, *args, **kwargs):
        role = models.UserData.objects.get(fAuth_id=request.user.id).fRole.name
        if role == 'User':
            return redirect('user-dashboard')
        if role == 'Admin':
            return redirect('admin-dashboard')
        return redirect('home-page')
