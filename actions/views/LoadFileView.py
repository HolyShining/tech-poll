from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import View
from actions.models import SectionsModel, StagesModel, QuestionsModel
from actions.file import file_worker


class LoadFileView(View):
    def get(self, request, mode):
        return render(request, 'actions/load_from_file.html', {'mode': mode})

    def post(self, request, mode):
        file = request.FILES['loaded_file']
        file_context = file_worker(file)
        query_list = []

        if mode == 'section':
            for line in file_context:
                if not SectionsModel.objects.filter(name=line[0]).exists():
                    query_list.append(SectionsModel(name=line[0]))
                return redirect('load-file')
            if query_list:
                StagesModel.objects.bulk_create(query_list)

        if mode == 'stage':
            for line in file_context:
                try:
                    section_id = SectionsModel.objects.get(name=line[1]).pk
                    print(line[0], section_id)
                    if not StagesModel.objects.filter(name=line[0]).exists():
                        query_list.append(StagesModel(name=line[0], f_section_id=section_id))
                except SectionsModel.DoesNotExist:
                    messages.add_message(request,
                                         messages.ERROR,
                                         '{} does not exist'.format(line[1]))
                    return redirect('load-file')
            if query_list:
                StagesModel.objects.bulk_create(query_list)

        if mode == 'question':
            for line in file_context:
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
                        query_list.append(QuestionsModel(name=name, hint=hint, f_stage_id=stage_id))
                except SectionsModel.DoesNotExist:
                    messages.add_message(request,
                                         messages.ERROR,
                                         '{} does not exist'.format(line[1]))
                    return redirect('load-file')
            if query_list:
                QuestionsModel.objects.bulk_create(query_list)

        messages.add_message(request,
                             messages.SUCCESS,
                             'File successfully loaded!')
        return redirect('auth-routing')
