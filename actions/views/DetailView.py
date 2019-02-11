from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from authentication.decorators import admin_role_required


class DetailView(View):
    """Base class for all details in Actions app"""
    model = None
    template = None
    add_models = None

    @admin_role_required
    def get(self, request, object_id):
        # Render basic data
        obj = get_object_or_404(self.model, pk=object_id)
        return render(request, self.template, {'obj': obj})