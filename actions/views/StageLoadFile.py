from django.contrib import messages
from django.shortcuts import redirect

from actions.models import StagesModel, SectionsModel
from actions.views import LoadFile
from authentication.decorators import admin_role_required


class StageLoadFile(LoadFile):
    @admin_role_required
    def post(self, request):
        """
        Specified Stage load file for pattern
        'stage_name' 'section_name'
        also fetch existing objects
        """
        self.file = request.FILES['loaded_file']
        query_list = []
        for line in self.get_file_context():
            try:
                section_id = SectionsModel.objects.get(name=line[1]).pk
                print(line[0], section_id)
                if not StagesModel.objects.filter(name=line[0]).exists():
                    print('appended')
                    query_list.append(StagesModel(name=line[0], f_section_id=section_id))
            except SectionsModel.DoesNotExist:
                self.send_message(messages.ERROR,
                                  '{} does not exist'.format(line[1]))
        if query_list:
            StagesModel.objects.bulk_create(query_list)
            self.send_message(status=messages.SUCCESS,
                              message='File successfully loaded!')

        return redirect('auth-routing')
