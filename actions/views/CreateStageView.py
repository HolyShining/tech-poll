from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import View
from actions.models import SectionsModel, StagesModel


class CreateStageView(View):
    def get(self, request):
        sections = SectionsModel.objects.all()
        return render(request, 'actions/form_stages.html', {'sections': sections})

    def post(self, request):
        stage = StagesModel(name=request.POST['name'])
        stage.f_section_id = request.POST['section']
        messages.add_message(request,
                             messages.SUCCESS,
                             'Section "{}" created successfully!'.format(stage.name))
        stage.save()
        return redirect('auth-routing')
