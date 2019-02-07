from abc import abstractmethod
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.base import View

from actions.file import file_worker
from actions.models import SectionsModel
from actions.interfaces import ISendMessage


class LoadFile(View, ISendMessage):
    request = None
    file = None
    _query_list = []

    def get(self, request):
        return render(request, 'actions/load_from_file.html')

    def send_message(self, status: int, message: str):
        messages.add_message(self.request,
                             status,
                             message)

    def get_file_context(self) -> list:
        return file_worker(self.file)





