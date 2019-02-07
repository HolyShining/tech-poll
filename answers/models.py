from django.db import models
from django.conf import settings
from actions.models import QuestionsModel, GradesModel


# Create your models here.

class AnswersModel(models.Model):
    class Meta:
        db_table = "answers"

    f_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='f_user')
    f_question = models.ForeignKey(QuestionsModel, on_delete=models.DO_NOTHING)
    answers_like = models.BooleanField()
    # f_expert = models.ForeignKey('UsersModel', on_delete=models.DO_NOTHING, null=True, related_name='f_expert')
    f_grade = models.ForeignKey(GradesModel, on_delete=models.DO_NOTHING)
