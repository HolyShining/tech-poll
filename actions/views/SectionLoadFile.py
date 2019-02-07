from django.contrib import messages
from django.shortcuts import redirect

from actions.models import SectionsModel
from actions.views import LoadFile
from authentication.decorators import admin_role_required


class SectionLoadFile(LoadFile):
    @admin_role_required
    def post(self, request):
        self.file = request.FILES['loaded_file']
        for line in self.get_file_context():
            if not SectionsModel.objects.filter(name=line[0]).exists():
                self._query_list.append(SectionsModel(name=line[0]))
        if self._query_list:
            SectionsModel.objects.bulk_create(self._query_list)
            self.send_message(status=messages.SUCCESS,
                              message='File successfully loaded!')
            self._query_list = []

        return redirect('auth-routing')
