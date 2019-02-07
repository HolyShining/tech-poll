from django.db import models


class QuestionsModel(models.Model):
    class Meta:
        db_table = "questions"
        ordering = ['id']

    name = models.TextField(max_length=255, default=None)
    hint = models.TextField(max_length=300, default=None)
    f_stage = models.ForeignKey('StagesModel', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
