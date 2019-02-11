from functools import wraps
from django.shortcuts import redirect

from authentication.models import UserData


def admin_role_required(function):
    """Check if user have got a Admin role and
     allow access for following function
     otherwise redirect to homepage if not logged
     or at routing if user has got another role"""
    @wraps(function)
    def wrapper(self, request, *args, **kwargs):
        try:
            if UserData.objects.get(f_auth_id=request.user.id).f_role.name == 'Admin':
                return function(self, request, *args, **kwargs)
            else:
                redirect('auth-routing')
        except UserData.DoesNotExist:
            return redirect('home-page')

    return wrapper
