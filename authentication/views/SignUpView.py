from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View
from authentication import models
from authentication.PasswordGenerator import get_password, randint
from authentication.decorators import admin_role_required


class SignUpView(View):
    @admin_role_required
    def get(self, request, *args, **kwargs):
        # Show form for creating user
        return render(request, 'authentication/createuser.html', {})

    @admin_role_required
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
                               f_auth=new_user)
        data.save()
        return render(request, 'authentication/user_created.html', {
            'username': usrname,
            'password': pswrd
        })
