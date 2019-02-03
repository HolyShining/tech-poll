from django.db import models

class StagesModel(models.Model):
    class Meta:
        db_table = "stages"

    name = models.CharField(max_length=60, default=None)
    f_section = models.ForeignKey('SectionsModel', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
