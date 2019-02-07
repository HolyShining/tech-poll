import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import AnswersModel
from actions.models import QuestionsModel, GradesModel


class AnswersView(View):
    def get(self, request, department_id):
        api_link = '/api/questions/{}'.format(str(department_id))
        return render(request, 'answers/answers.html', {'api_link': api_link})

    def post(self, request, department_id):
        json_string = str(request.body.decode('UTF-8'))
        answers = dict(json.loads(json_string))
        query_list = []
        print(answers)
        for question in answers:
            ans = AnswersModel()
            ans.f_question = QuestionsModel.objects.get(name=question)
            ans.f_user_id = request.user.id
            if answers[ans.f_question.name]['Like to do'] == 'Yes':
                ans.answers_like = True
            else:
                ans.answers_like = False
            ans.f_grade_id = GradesModel.objects.filter(name=answers[ans.f_question.name]['Self-estimate']).first().id
            query_list.append(ans)
            # print(ans.f_grade)

        print(query_list)
        if query_list:
            AnswersModel.objects.bulk_create(query_list)

        return HttpResponse('Success! JSON received and answers saved.')
