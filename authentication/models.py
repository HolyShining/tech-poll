from django.db import models
from django.conf import settings


# Create your models here.

class UserData(models.Model):
    class Meta:
        db_table = 'user_data'

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    encrypted_pass = models.CharField(max_length=16, null=True)
    fAuth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fRole = models.ForeignKey('RolesModel', on_delete=models.DO_NOTHING, default=2)

    def __str__(self):
        return '{name} {surname}'.format(name=self.name, surname=self.surname)


class PermissionsModel(models.Model):
    class Meta:
        db_table = "permissions"

    code_name = models.CharField(max_length=60, default="null")


class RolesModel(models.Model):
    class Meta:
        db_table = "roles"

    name = models.CharField(max_length=60, default="null")
    permissions = models.ManyToManyField('PermissionsModel')
