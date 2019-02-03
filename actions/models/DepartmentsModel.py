from django.db import models


class DepartmentsModel(models.Model):
    class Meta:
        db_table = "departments"

    name = models.CharField(max_length=100, default=None)
    questions = models.ManyToManyField('QuestionsModel')
