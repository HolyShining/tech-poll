from django.shortcuts import redirect
from django.views.generic import View


class HomeView(View):
    """Cap for base url"""
    def get(self, request, *args, **kwargs):
        return redirect('auth-routing')
