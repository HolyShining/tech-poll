from django.shortcuts import redirect, get_object_or_404
from actions.models import GradesModel
from django.contrib import messages
from actions.views import DetailView


class GradeDetailView(DetailView):
    model = GradesModel
    template = 'actions/form_grade.html'

    def post(self, request, object_id):
        # Update Grade record
        grade = get_object_or_404(GradesModel, pk=object_id)
        grade.name = request.POST['name']
        grade.save()
        messages.add_message(request, messages.SUCCESS, 'Section updated successfully')
        return redirect('auth-routing')
