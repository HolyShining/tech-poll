from django.shortcuts import redirect, get_object_or_404
from actions.models import SectionsModel
from django.contrib import messages
from actions.views import DetailView


class SectionDetailView(DetailView):
    model = SectionsModel
    template = 'actions/form_sections.html'

    def post(self, request, object_id):
        # Update section
        section = get_object_or_404(SectionsModel, pk=object_id)
        section.name = request.POST['name']
        section.save()
        messages.add_message(request, messages.SUCCESS, 'Section updated successfully')
        return redirect('auth-routing')
