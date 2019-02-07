from django.contrib import messages
from django.shortcuts import redirect

from actions.models import QuestionsModel, StagesModel
from actions.views import LoadFile


class QuestionLoadFile(LoadFile):
    def post(self, request):
        self.file = request.FILES['loaded_file']
        for line in self.get_file_context():
            if len(line) == 3:
                name = line[0]
                hint = line[1]
                stage_id = StagesModel.objects.get(name=line[2]).pk
            else:
                name = line[0]
                hint = ""
                stage_id = StagesModel.objects.get(name=line[1]).pk

            try:
                if not StagesModel.objects.filter(name=name).exists():
                    self._query_list.append(QuestionsModel(name=name, hint=hint, f_stage_id=stage_id))
            except StagesModel.DoesNotExist:
                self.send_message(messages.ERROR,
                                  '{} does not exist'.format(line[1]))
        if self._query_list:
            QuestionsModel.objects.bulk_create(self._query_list)
            self.send_message(status=messages.SUCCESS,
                              message='File successfully loaded!')
            self._query_list = []

        return redirect('auth-routing')