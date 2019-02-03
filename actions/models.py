from django.db import models


# Create your models here.

class SectionsModel(models.Model):
    class Meta:
        db_table = "sections"

    name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name


class StagesModel(models.Model):
    class Meta:
        db_table = "stages"

    name = models.CharField(max_length=60, default=None)
    f_section = models.ForeignKey('SectionsModel', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class QuestionsModel(models.Model):
    class Meta:
        db_table = "questions"

    name = models.TextField(max_length=255, default=None)
    hint = models.TextField(max_length=300, default=None)
    f_stage = models.ForeignKey('StagesModel', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


