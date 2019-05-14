from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    accepted_tos = models.IntegerField(default=0)
