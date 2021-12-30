from django.db import models

from django.contrib.auth.models import User

class Ad(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    sold = models.BooleanField(default=False)

class Owner(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    