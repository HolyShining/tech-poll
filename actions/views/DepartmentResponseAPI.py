from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from actions.models import QuestionsModel, DepartmentsModel, SectionsModel, StagesModel


class DepartmentResponse(View):
    def get(self, request, department_id):
        try:
            dep = DepartmentsModel.objects.get(id=department_id)
        except DepartmentsModel.DoesNotExist:
            return HttpResponse('Department not found')
        result = {'department': dep.name,
                  'questions': list(),
                  'stages': list(),
                  'sections': list()}

        print(request.user.id)
        for question in list(dep.questions.all()):
            result['questions'].append({'name': question.name, 'stages': question.f_stage.name, 'hint':question.hint})
            result['stages'].append({'name': question.f_stage.name, 'section': question.f_stage.f_section.name})
            result['sections'].append({'name': question.f_stage.f_section.name})

        result['stages'] = [dict(names) for names in set(tuple(item.items()) for item in result['stages'])]
        result['sections'] = [dict(names) for names in set(tuple(item.items()) for item in result['sections'])]
        return JsonResponse(result)
