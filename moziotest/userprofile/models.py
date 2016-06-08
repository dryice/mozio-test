from django.contrib.gis.db import models
from django.conf import settings


UserModel = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel)
    phone_number = models.CharField(max_length = 15)
    language = models.CharField(max_length = 15)
    currency = models.CharField(max_length = 15)

    def __str__(self):
        return self.user


class ServiceArea(models.Model):
    provider = models.ForeignKey(UserModel)
    name = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    area = models.PolygonField()

