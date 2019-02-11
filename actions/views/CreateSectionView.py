from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import View
from actions.models import SectionsModel
from authentication.decorators import admin_role_required


class CreateSectionView(View):
    @admin_role_required
    def get(self, request, *args, **kwargs):
        return render(request, 'actions/form_sections.html')

    @admin_role_required
    def post(self, request):
        # Show message when creating section
        section = SectionsModel(name=request.POST['name'])
        messages.add_message(request,
                             messages.SUCCESS,
                             'Section "{}" created successfully!'.format(section.name))
        section.save()
        return redirect('auth-routing')
