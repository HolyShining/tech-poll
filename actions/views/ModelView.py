from django.shortcuts import render, redirect
from django.views.generic import View

from actions.models import SectionsModel, StagesModel, QuestionsModel, DepartmentsModel, GradesModel
from authentication.decorators import admin_role_required


class ModelView(View):
    """Base class to View model"""
    model = None  # Model class
    name = None  # Human name of object
    edit = None  # Name of edit URL

    @admin_role_required
    def get(self, request):
        """Show all object for specified model"""
        obj = self.model.objects.all()
        return render(request, 'actions/model_view.html', {'objects': obj,
                                                           'name': self.name,
                                                           'edit': self.edit})


# Child classes

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


class DepartmentsView(ModelView):
    model = DepartmentsModel
    name = "Departments"
    edit = 'edit-department'


class GradesView(ModelView):
    model = GradesModel
    name = "Grades"
    edit = 'edit-grade'
