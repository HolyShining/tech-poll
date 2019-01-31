from django.contrib.auth.models import User
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
            user = User.objects.get(username=usrname)
            print("*** {} NOT EXIST ***".format(usrname.upper()))
        except User.DoesNotExist:
            pass
        else:
            usrname += str(randint(0,9))
            print("*** {} EXIST ***".format(usrname.upper()))
        new_user = User(username=usrname, password=pswrd)
        new_user.save()
        data = models.UserData(name=request.POST['name'],
                               surname=request.POST['surname'],
                               fAuth=new_user)
        data.save()
        return render(request, 'authentication/user_created.html', {
                                                                    'username': usrname,
                                                                    'password': pswrd
                                                                    })
