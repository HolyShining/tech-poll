from django.db import models


class SectionsModel(models.Model):
    class Meta:
        db_table = "sections"
        ordering = ['name']

    name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name
