from abc import abstractmethod
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.base import View

from actions.file import file_worker
from actions.models import SectionsModel
from actions.interfaces import ISendMessage
from authentication.decorators import admin_role_required


class LoadFile(View, ISendMessage):
    """Base class for loading files"""
    request = None
    file = None

    @admin_role_required
    def get(self, request):
        return render(request, 'actions/load_from_file.html')

    def send_message(self, status: int, message: str):
        """Send message to user with selected status and specified message"""
        messages.add_message(self.request,
                             status,
                             message)

    def get_file_context(self) -> list:
        """Translate binary file into list"""
        return file_worker(self.file)





