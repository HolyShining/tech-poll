from django.db import models
from django.conf import settings


# Create your models here.

class UserData(models.Model):
    class Meta:
        db_table = 'UserData'

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    fAuth = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
