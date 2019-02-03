from django.shortcuts import render, redirect
from django.views.generic import View

from actions.models import SectionsModel, StagesModel, QuestionsModel


class ModelView(View):
    model = None
    name = None
    edit = None

    def get(self, request, *args, **kwargs):
        obj = self.model.objects.all()
        return render(request, 'actions/model_view.html', {'objects': obj,
                                                           'name': self.name,
                                                           'edit': self.edit})


class SectionView(ModelView):
    model = SectionsModel
    name = "Sections"
    edit = 'edit-section'


class StagesView(ModelView):
    model = StagesModel
    name = "Stages"
    edit = 'edit-stage'


class QuestionsView(ModelView):
    model = QuestionsModel
    name = "Questions"
    edit = 'edit-question'
