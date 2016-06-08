from django.db import models
from django.conf import settings


UserModel = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel)
    phone_number = models.CharField(max_length = 15)
    language = models.CharField(max_length = 15)
    currency = models.CharField(max_length = 15)

    def __str__(self):
        return self.user
