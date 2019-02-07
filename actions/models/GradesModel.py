from django.db import models


class GradesModel(models.Model):
    class Meta:
        db_table = "grades"

    name = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name.title()
