from django.contrib import messages
from django.shortcuts import redirect

from actions.models import StagesModel, SectionsModel
from actions.views import LoadFile


class StageLoadFile(LoadFile):
    def post(self, request):
        self.file = request.FILES['loaded_file']
        for line in self.get_file_context():
            try:
                section_id = SectionsModel.objects.get(name=line[1]).pk
                print(line[0], section_id)
                if not StagesModel.objects.filter(name=line[0]).exists():
                    self._query_list.append(StagesModel(name=line[0], f_section_id=section_id))
            except SectionsModel.DoesNotExist:
                self.send_message(messages.ERROR,
                                  '{} does not exist'.format(line[1]))
        if self._query_list:
            StagesModel.objects.bulk_create(self._query_list)
            self.send_message(status=messages.SUCCESS,
                              message='File successfully loaded!')
            self._query_list = []

        return redirect('auth-routing')
