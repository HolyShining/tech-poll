import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import AnswersModel
from actions.models import QuestionsModel


class AnswersView(View):
    def get(self, request, department_id):
        api_link = '/api/questions/{}'.format(str(department_id))
        return render(request, 'answers/answers.html', {'api_link': api_link})

    def post(self, request):
        json_string = str(request.body.decode('UTF-8'))
        answers = dict(json.loads(json_string))
        query_list = []

        for question in answers:
            ans = AnswersModel()
            ans.f_question = QuestionsModel.objects.get(name=question)
            ans.f_user_id = request.user.id
            if answers[ans.f_question.name]['Like to do'] == 'Yes':
                ans.answers_like = True
            else:
                ans.answers_like = False
            ans.f_grade = answers[ans.f_question.name]['Self-estimate']
            query_list.append(ans)

        if query_list:
            AnswersModel.objects.bulk_create(query_list)

        return HttpResponse('Success! JSON received and answers saved.')
