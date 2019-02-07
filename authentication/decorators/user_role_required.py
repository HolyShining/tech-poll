from functools import wraps
from django.shortcuts import redirect

from authentication.models import UserData


def user_role_required(function):
    @wraps(function)
    def wrapper(self, request, *args, **kwargs):
        try:
            if UserData.objects.get(f_auth_id=request.user.id).f_role.name == 'User' or \
                    UserData.objects.get(f_auth_id=request.user.id).f_role.name == 'Admin':
                return function(self, request, *args, **kwargs)
        finally:
            return redirect('home-page')

    return wrapper
