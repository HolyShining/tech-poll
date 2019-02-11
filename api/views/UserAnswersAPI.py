from django.http import JsonResponse, HttpResponse
from django.views import View

from answers.models import AnswersModel
from authentication.models import UserData


class UserAnswersAPI(View):
    def get(self, request, user):
        """
        API that return all information about user in JSON format
        """
        name, surname = user.split('-')
        try:
            obj = UserData.objects.get(name__iexact=name, surname__iexact=surname)
        except UserData.DoesNotExist:
            return HttpResponse('User not found')
        finalJSON = {'User': '{} {}'.format(name, surname).title(),
                     'Department': obj.departmentsmodel_set.first().name,
                     'Answers': dict()}

        for answer in list(AnswersModel.objects.filter(f_user=obj.f_auth)):
            finalJSON['Answers'][answer.f_question.name] = {}
            if answer.answers_like:
                like_to_do = 'Yes'
            else:
                like_to_do = 'No'
            finalJSON['Answers'][answer.f_question.name]['Like to do'] = like_to_do
            finalJSON['Answers'][answer.f_question.name]['Self-estimate'] = answer.f_grade.name
        return JsonResponse(finalJSON)
