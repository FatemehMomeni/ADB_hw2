from django.db import models


class Users(models.Model):
    name = models.TextField()
    family = models.TextField()
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    tel = models.BigIntegerField()
    address = models.TextField()
    gender = models.TextField()

    objects = models.Manager()
