from django.db import models


# Create your models here.

class SectionsModel(models.Model):
    class Meta:
        db_table = "sections"

    name = models.CharField(max_length=60, default=None)
