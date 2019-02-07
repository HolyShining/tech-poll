from django.db import models
from django.conf import settings


class UserData(models.Model):
    class Meta:
        db_table = 'user_data'
        ordering = ['id']

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    encrypted_pass = models.CharField(max_length=16, null=True)
    f_auth = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    f_role = models.ForeignKey('RolesModel', on_delete=models.DO_NOTHING, default=2)

    def __str__(self):
        return '{name} {surname}'.format(name=self.name, surname=self.surname).title()
