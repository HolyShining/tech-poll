from django.contrib import messages
from django.shortcuts import redirect

from actions.models import SectionsModel
from actions.views import LoadFile
from authentication.decorators import admin_role_required


class SectionLoadFile(LoadFile):
    @admin_role_required
    def post(self, request):
        self.file = request.FILES['loaded_file']
        query_list = []
        for line in self.get_file_context():
            if not SectionsModel.objects.filter(name=line[0]).exists():
                query_list.append(SectionsModel(name=line[0]))
        if query_list:
            SectionsModel.objects.bulk_create(query_list)
            self.send_message(status=messages.SUCCESS,
                              message='File successfully loaded!')

        return redirect('auth-routing')
