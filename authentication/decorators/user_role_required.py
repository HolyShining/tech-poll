from functools import wraps
from django.shortcuts import redirect

from authentication.models import UserData


def user_role_required(function):
    """Check if user logged in and allowed for actions in system"""
    @wraps(function)
    def wrapper(self, request, *args, **kwargs):
        try:
            if UserData.objects.get(f_auth_id=request.user.id).f_role.name == 'User' or \
                    UserData.objects.get(f_auth_id=request.user.id).f_role.name == 'Admin':
                return function(self, request, *args, **kwargs)
            else:
                return redirect('auth-routing')
        except UserData.DoesNotExist:
            return redirect('home-page')

    return wrapper
