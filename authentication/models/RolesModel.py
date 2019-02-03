from django.db import models


class RolesModel(models.Model):
    class Meta:
        db_table = "roles"

    name = models.CharField(max_length=60, default="null")
    permissions = models.ManyToManyField('PermissionsModel')
