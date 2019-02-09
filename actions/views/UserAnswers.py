from django.http import JsonResponse
from django.views import View

from answers.models import AnswersModel


class UserAnswerResponse(View):
    def get(self, request):
        finalJSON = {'User': 'Nickname',
                     'Department': 'WebUI',
                     'Answers': dict()}

        print(AnswersModel.objects.filter(f_user_id=23))
        for answer in list(AnswersModel.objects.filter(f_user_id=23)):
            finalJSON['Answers'][answer.f_question.name] = {}
            if answer.answers_like:
                like_to_do = 'Yes'
            else:
                like_to_do = 'No'
            finalJSON['Answers'][answer.f_question.name]['Like to do'] = like_to_do
            finalJSON['Answers'][answer.f_question.name]['Self-estimate'] = answer.f_grade.name
        return JsonResponse(finalJSON)
