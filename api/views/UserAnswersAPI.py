from django.http import JsonResponse
from django.views import View

from answers.models import AnswersModel
from authentication.models import UserData


class UserAnswersAPI(View):
    def get(self, request, user):
        name, surname = user.split('-')
        obj = UserData.objects.get(name__iexact=name, surname__iexact=surname)
        print()
        finalJSON = {'User': '{} {}'.format(name, surname),
                     'Department': obj.departmentsmodel_set.first().name,
                     'Answers': dict()}

        print(AnswersModel.objects.filter(f_user=obj.f_auth))
        for answer in list(AnswersModel.objects.filter(f_user=obj.f_auth)):
            finalJSON['Answers'][answer.f_question.name] = {}
            if answer.answers_like:
                like_to_do = 'Yes'
            else:
                like_to_do = 'No'
            finalJSON['Answers'][answer.f_question.name]['Like to do'] = like_to_do
            finalJSON['Answers'][answer.f_question.name]['Self-estimate'] = answer.f_grade.name
        return JsonResponse(finalJSON)
