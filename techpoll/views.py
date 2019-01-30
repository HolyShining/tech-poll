from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'application/homepage.html', {})

class RedirectingView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'application/redirecting.html', {})
