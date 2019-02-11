from django.shortcuts import render, redirect, get_object_or_404
from actions.models import SectionsModel, StagesModel
from django.contrib import messages
from actions.views import DetailView


class StageDetailView(DetailView):
    model = StagesModel
    template = 'actions/form_stages.html'
    add_models = SectionsModel

    def get(self, request, object_id):
        # Load linked section for stage and render it
        obj = get_object_or_404(self.model, pk=object_id)
        sections = self.add_models.objects.all()
        return render(request, self.template, {'obj': obj,
                                               'sections': sections})

    def post(self, request, object_id):
        # Update stage
        stage = get_object_or_404(self.model, pk=object_id)
        stage.name = request.POST['name']
        stage.f_section_id = request.POST['section']
        stage.save()
        messages.add_message(request, messages.SUCCESS, 'Stage updated successfully')
        return redirect('auth-routing')
