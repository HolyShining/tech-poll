import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import AnswersModel
from actions.models import QuestionsModel, GradesModel
from authentication.decorators import user_role_required


class AnswersView(View):
    @user_role_required
    def get(self, request, department):
        # Generate link for response from client and render client app
        api_link = '/api/questions/{}'.format(department)
        return render(request, 'answers/answers.html', {'api_link': api_link})

    def post(self, request, department):
        """Receive JSON data from client-part, parse belongs to
        AnswerModel rules and send response if successful saved data """
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

            if answers[ans.f_question.name]['Self-estimate'] is None:
                # Additional validate to prevent db nullable exception
                ans.f_grade_id = GradesModel.objects.get(name='None').id
            else:
                ans.f_grade_id = GradesModel.objects.get(name=answers[ans.f_question.name]['Self-estimate']).id
            query_list.append(ans)

        if query_list:
            # Send query to db if query exist
            AnswersModel.objects.bulk_create(query_list)

        return HttpResponse('Success! JSON received and answers saved.')
