from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.messages import get_messages


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        messages = get_messages(request)
        view_message = None
        for message in messages:
            view_message = message
        return render(request, 'application/homepage.html', {'msg': view_message})


class RedirectingView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'application/redirecting.html', {})
