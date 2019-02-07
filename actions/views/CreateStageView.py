from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import View
from actions.models import SectionsModel, StagesModel
from authentication.decorators import admin_role_required


class CreateStageView(View):
    @admin_role_required
    def get(self, request):
        sections = SectionsModel.objects.all()
        return render(request, 'actions/form_stages.html', {'sections': sections})

    @admin_role_required
    def post(self, request):
        stage = StagesModel(name=request.POST['name'])
        stage.f_section_id = request.POST['section']
        messages.add_message(request,
                             messages.SUCCESS,
                             'Section "{}" created successfully!'.format(stage.name))
        stage.save()
        return redirect('auth-routing')
