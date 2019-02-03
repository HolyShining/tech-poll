from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from authentication import models


class UserDetail(View):
    def get(self, request, user_id):
        usr = get_object_or_404(models.UserData, pk=user_id)
        return render(request, 'authentication/user_details.html', {'object': usr})
