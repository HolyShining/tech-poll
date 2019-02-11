from django.contrib import messages
from django.shortcuts import redirect

from actions.models import QuestionsModel, StagesModel
from actions.views import LoadFile
from authentication.decorators import admin_role_required


class QuestionLoadFile(LoadFile):
    @admin_role_required
    def post(self, request):
        self.file = request.FILES['loaded_file']
        query_list = []
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
                if not QuestionsModel.objects.filter(name=name).exists():
                    query_list.append(QuestionsModel(name=name, hint=hint, f_stage_id=stage_id))
            except QuestionsModel.DoesNotExist:
                self.send_message(messages.ERROR,
                                  '{} does not exist'.format(line[1]))
        if query_list:
            QuestionsModel.objects.bulk_create(query_list)
            self.send_message(status=messages.SUCCESS,
                              message='File successfully loaded!')

        return redirect('auth-routing')
