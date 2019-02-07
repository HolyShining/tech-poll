from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import View
from actions.models import SectionsModel


class CreateSectionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'actions/form_sections.html')

    def post(self, request):
        section = SectionsModel(name=request.POST['name'])
        print(section)
        messages.add_message(request,
                             messages.SUCCESS,
                             'Section "{}" created successfully!'.format(section.name))
        section.save()
        return redirect('auth-routing')
