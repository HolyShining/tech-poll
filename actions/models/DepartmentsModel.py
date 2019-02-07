from django.db import models
from authentication.models import UserData


class DepartmentsModel(models.Model):
    class Meta:
        db_table = "departments"
        ordering = ['id']

    name = models.CharField(max_length=100, default=None)
    questions = models.ManyToManyField('QuestionsModel')
    users = models.ManyToManyField(UserData)

    def __str__(self):
        return self.name
